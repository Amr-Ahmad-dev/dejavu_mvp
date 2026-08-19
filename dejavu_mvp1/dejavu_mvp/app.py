"""
Déjà Vu — Smart Outing Recommendation Platform (MVP)

Core flows implemented from the InnovEgypt research:
  1. Budget-first, vibe-first discovery ("Reverse Budget-First Search" + "Vibe & Mood Filtering")
  2. Group Swipe-to-Match rooms (highest-scored idea, 8/9 desirability/feasibility)
  3. Verified-visit reviews (trust/authenticity cluster)
  4. Hidden-gem surfacing (discovery cluster)

Architecture: single-file Flask app, SQLite via sqlite3, Jinja2 templates.
"""
import random
import sqlite3
import string
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g

DATABASE = "dejavu.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-change-in-production"


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def execute_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    lastid = cur.lastrowid
    cur.close()
    return lastid


def gen_room_code(length=5):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


# ---------------------------------------------------------------------------
# Context processors — categories/vibes available in every template (navbar filters)
# ---------------------------------------------------------------------------
@app.context_processor
def inject_globals():
    categories = query_db("SELECT * FROM category ORDER BY name")
    vibes = query_db("SELECT * FROM vibe ORDER BY name")
    return dict(nav_categories=categories, nav_vibes=vibes, current_year=datetime.now().year)


# ---------------------------------------------------------------------------
# Core discovery routes
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    """Landing page: budget / group size / area quick-filter, per the wireframe."""
    hidden_gems = query_db(
        """SELECT p.*, c.name AS category_name, c.icon AS category_icon,
                  ROUND(AVG(r.rating), 1) AS avg_rating, COUNT(r.id) AS review_count
           FROM place p
           JOIN category c ON c.id = p.category_id
           LEFT JOIN review r ON r.place_id = p.id
           WHERE p.is_hidden_gem = 1
           GROUP BY p.id
           ORDER BY RANDOM() LIMIT 4"""
    )
    areas = [row["area"] for row in query_db("SELECT DISTINCT area FROM place ORDER BY area")]
    return render_template("index.html", hidden_gems=hidden_gems, areas=areas)


@app.route("/discover")
def discover():
    """
    Main discovery/results page. Implements 'Reverse Budget-First Search':
    user sets a max budget + optional category/vibe/area, we surface matches.
    """
    budget_max = request.args.get("budget_max", type=int)
    category_id = request.args.get("category_id", type=int)
    vibe_id = request.args.get("vibe_id", type=int)
    area = request.args.get("area", "").strip()
    group_size = request.args.get("group_size", type=int)
    sort = request.args.get("sort", "recommended")

    sql = """
        SELECT p.*, c.name AS category_name, c.icon AS category_icon,
               ROUND(AVG(r.rating), 1) AS avg_rating, COUNT(DISTINCT r.id) AS review_count
        FROM place p
        JOIN category c ON c.id = p.category_id
        LEFT JOIN review r ON r.place_id = p.id
    """
    joins = []
    where = []
    params = []

    if vibe_id:
        joins.append("JOIN place_vibe pv ON pv.place_id = p.id AND pv.vibe_id = ?")
        params.append(vibe_id)
    if budget_max:
        where.append("p.price_per_person <= ?")
        params.append(budget_max)
    if category_id:
        where.append("p.category_id = ?")
        params.append(category_id)
    if area:
        where.append("p.area = ?")
        params.append(area)

    sql = sql.replace("LEFT JOIN review", " ".join(joins) + " LEFT JOIN review") if joins else sql
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " GROUP BY p.id"

    if sort == "price_low":
        sql += " ORDER BY p.price_per_person ASC"
    elif sort == "price_high":
        sql += " ORDER BY p.price_per_person DESC"
    elif sort == "rating":
        sql += " ORDER BY avg_rating DESC"
    else:
        sql += " ORDER BY p.is_hidden_gem DESC, avg_rating DESC"

    places = query_db(sql, params)

    total_estimate = None
    if budget_max and group_size:
        total_estimate = budget_max * group_size

    return render_template(
        "discover.html",
        places=places,
        budget_max=budget_max,
        category_id=category_id,
        vibe_id=vibe_id,
        area=area,
        group_size=group_size,
        sort=sort,
        total_estimate=total_estimate,
    )


@app.route("/place/<int:place_id>")
def place_detail(place_id):
    place = query_db(
        """SELECT p.*, c.name AS category_name, c.icon AS category_icon
           FROM place p JOIN category c ON c.id = p.category_id
           WHERE p.id = ?""",
        (place_id,),
        one=True,
    )
    if not place:
        flash("Place not found.", "error")
        return redirect(url_for("discover"))

    vibes = query_db(
        """SELECT v.* FROM vibe v
           JOIN place_vibe pv ON pv.vibe_id = v.id
           WHERE pv.place_id = ?""",
        (place_id,),
    )
    reviews = query_db(
        "SELECT * FROM review WHERE place_id = ? ORDER BY created_at DESC", (place_id,)
    )
    avg_rating_row = query_db(
        "SELECT ROUND(AVG(rating),1) AS avg_rating, COUNT(*) AS cnt FROM review WHERE place_id = ?",
        (place_id,),
        one=True,
    )
    return render_template(
        "place_detail.html",
        place=place,
        vibes=vibes,
        reviews=reviews,
        avg_rating=avg_rating_row["avg_rating"],
        review_count=avg_rating_row["cnt"],
    )


@app.route("/place/<int:place_id>/review", methods=["POST"])
def add_review(place_id):
    """Verified-visit review submission (MVP simulates GPS/receipt check with a checkbox)."""
    reviewer_name = request.form.get("reviewer_name", "").strip() or "Anonymous"
    rating = request.form.get("rating", type=int)
    comment = request.form.get("comment", "").strip()
    verified = 1 if request.form.get("verified_visit") == "on" else 0

    if not rating or not (1 <= rating <= 5):
        flash("Please select a rating between 1 and 5.", "error")
        return redirect(url_for("place_detail", place_id=place_id))

    execute_db(
        """INSERT INTO review (place_id, reviewer_name, rating, comment, verified_visit)
           VALUES (?, ?, ?, ?, ?)""",
        (place_id, reviewer_name, rating, comment, verified),
    )
    flash("Review submitted — thanks for keeping Déjà Vu trustworthy!", "success")
    return redirect(url_for("place_detail", place_id=place_id))


# ---------------------------------------------------------------------------
# Group Swipe-to-Match (top-scoring idea from ideation)
# ---------------------------------------------------------------------------
@app.route("/swipe/new", methods=["GET", "POST"])
def swipe_new():
    if request.method == "POST":
        host_name = request.form.get("host_name", "").strip() or "Host"
        budget_max = request.form.get("budget_max", type=int)
        category_id = request.form.get("category_id", type=int) or None

        code = gen_room_code()
        while query_db("SELECT id FROM room WHERE code = ?", (code,), one=True):
            code = gen_room_code()

        room_id = execute_db(
            """INSERT INTO room (code, host_name, budget_max, category_id, status)
               VALUES (?, ?, ?, ?, 'open')""",
            (code, host_name, budget_max, category_id),
        )
        execute_db(
            "INSERT INTO room_member (room_id, member_name) VALUES (?, ?)",
            (room_id, host_name),
        )
        return redirect(url_for("swipe_room", code=code, member=host_name))

    categories = query_db("SELECT * FROM category ORDER BY name")
    return render_template("swipe_new.html", categories=categories)


@app.route("/swipe/join", methods=["POST"])
def swipe_join():
    code = request.form.get("code", "").strip().upper()
    member_name = request.form.get("member_name", "").strip() or "Guest"
    room = query_db("SELECT * FROM room WHERE code = ?", (code,), one=True)
    if not room:
        flash("Room not found. Check the code and try again.", "error")
        return redirect(url_for("swipe_new"))

    existing = query_db(
        "SELECT id FROM room_member WHERE room_id = ? AND member_name = ?",
        (room["id"], member_name),
        one=True,
    )
    if not existing:
        execute_db(
            "INSERT INTO room_member (room_id, member_name) VALUES (?, ?)",
            (room["id"], member_name),
        )
    return redirect(url_for("swipe_room", code=code, member=member_name))


@app.route("/swipe/<code>")
def swipe_room(code):
    room = query_db("SELECT * FROM room WHERE code = ?", (code,), one=True)
    if not room:
        flash("Room not found.", "error")
        return redirect(url_for("swipe_new"))

    member = request.args.get("member", "").strip()
    members = query_db(
        "SELECT * FROM room_member WHERE room_id = ? ORDER BY joined_at", (room["id"],)
    )

    if room["status"] == "matched":
        place = query_db("SELECT * FROM place WHERE id = ?", (room["matched_place_id"],), one=True)
        return render_template("swipe_matched.html", room=room, place=place, members=members)

    # candidate places: filtered by room budget/category, excluding ones this member already swiped
    sql = """SELECT p.*, c.name AS category_name, c.icon AS category_icon
              FROM place p JOIN category c ON c.id = p.category_id
              WHERE p.id NOT IN (
                  SELECT place_id FROM room_swipe WHERE room_id = ? AND member_name = ?
              )"""
    params = [room["id"], member]
    if room["budget_max"]:
        sql += " AND p.price_per_person <= ?"
        params.append(room["budget_max"])
    if room["category_id"]:
        sql += " AND p.category_id = ?"
        params.append(room["category_id"])
    sql += " ORDER BY p.is_hidden_gem DESC LIMIT 1"

    next_place = query_db(sql, params, one=True)

    return render_template(
        "swipe_room.html", room=room, member=member, members=members, next_place=next_place
    )


@app.route("/swipe/<code>/vote", methods=["POST"])
def swipe_vote(code):
    room = query_db("SELECT * FROM room WHERE code = ?", (code,), one=True)
    if not room:
        return jsonify({"error": "room not found"}), 404

    member = request.form.get("member", "").strip()
    place_id = request.form.get("place_id", type=int)
    liked = 1 if request.form.get("liked") == "1" else 0

    execute_db(
        """INSERT OR IGNORE INTO room_swipe (room_id, member_name, place_id, liked)
           VALUES (?, ?, ?, ?)""",
        (room["id"], member, place_id, liked),
    )

    # Check for a match: every current member liked this place
    if liked:
        member_count = query_db(
            "SELECT COUNT(*) AS c FROM room_member WHERE room_id = ?", (room["id"],), one=True
        )["c"]
        like_count = query_db(
            """SELECT COUNT(DISTINCT member_name) AS c FROM room_swipe
               WHERE room_id = ? AND place_id = ? AND liked = 1""",
            (room["id"], place_id),
            one=True,
        )["c"]
        if member_count > 0 and like_count >= member_count:
            execute_db(
                "UPDATE room SET status = 'matched', matched_place_id = ? WHERE id = ?",
                (place_id, room["id"]),
            )
            return jsonify({"matched": True})

    return jsonify({"matched": False})


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
