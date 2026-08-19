"""
Seed script for Déjà Vu.
Populates categories, vibes, and a realistic set of Cairo places
(restaurants, cafés, parks, entertainment, shopping — per the BMC's
key partners) with verified reviews and hidden-gem flags, matching
the research clusters: Financial Transparency, Authenticity/Verification,
Vibe & Mood, and Hidden Gems.
"""
import sqlite3
import random

DB_PATH = "dejavu.db"

CATEGORIES = [
    ("Restaurant", "🍽️"),
    ("Café", "☕"),
    ("Park", "🌳"),
    ("Entertainment", "🎮"),
    ("Shopping", "🛍️"),
]

VIBES = [
    ("Chill & Quiet", "🌙"),
    ("Study-Friendly", "📚"),
    ("Loud & Lively", "🎉"),
    ("Romantic", "💛"),
    ("Outdoorsy", "🌿"),
    ("Aesthetic / Instagrammable", "📸"),
    ("Budget-Friendly", "💸"),
    ("Late-Night", "🌃"),
]

# name, category, area, price_per_person (EGP), hidden_gem, vibes[]
PLACES = [
    ("Left Bank", "Restaurant", "Zamalek", 450, 0, ["Romantic", "Aesthetic / Instagrammable"]),
    ("Beano's", "Café", "Downtown Cairo", 120, 0, ["Study-Friendly", "Chill & Quiet"]),
    ("El Fishawy", "Café", "Khan El Khalili", 90, 0, ["Loud & Lively", "Aesthetic / Instagrammable"]),
    ("Sequoia", "Restaurant", "Zamalek", 600, 0, ["Romantic", "Outdoorsy"]),
    ("Cairo Jazz Club", "Entertainment", "Agouza", 350, 0, ["Loud & Lively", "Late-Night"]),
    ("Al-Azhar Park", "Park", "Al-Darb Al-Ahmar", 40, 0, ["Outdoorsy", "Chill & Quiet"]),
    ("Grandma's House Café", "Café", "Maadi", 100, 1, ["Study-Friendly", "Budget-Friendly", "Chill & Quiet"]),
    ("Tabla Restaurant", "Restaurant", "Mohandessin", 250, 0, ["Loud & Lively"]),
    ("Cook Door", "Restaurant", "Nasr City", 180, 0, ["Budget-Friendly"]),
    ("The Tap East", "Entertainment", "New Cairo", 400, 0, ["Loud & Lively", "Late-Night"]),
    ("Hero's Nation", "Entertainment", "New Cairo", 300, 0, ["Loud & Lively"]),
    ("Zooba", "Restaurant", "Zamalek", 150, 0, ["Budget-Friendly", "Aesthetic / Instagrammable"]),
    ("Loft 59", "Café", "Sheikh Zayed", 160, 1, ["Aesthetic / Instagrammable", "Chill & Quiet"]),
    ("Family Park", "Park", "Nasr City", 30, 0, ["Outdoorsy", "Budget-Friendly"]),
    ("City Stars Mall", "Shopping", "Nasr City", 200, 0, ["Loud & Lively"]),
    ("Mall of Egypt", "Shopping", "6th of October", 220, 0, ["Loud & Lively"]),
    ("Km 28", "Restaurant", "Cairo-Alex Desert Road", 500, 0, ["Romantic", "Outdoorsy"]),
    ("Cilantro Zamalek", "Café", "Zamalek", 110, 0, ["Study-Friendly", "Chill & Quiet"]),
    ("Somabay Coffee Roastery", "Café", "Maadi", 130, 1, ["Aesthetic / Instagrammable", "Study-Friendly"]),
    ("Andrea Mariouteya", "Restaurant", "Haram", 280, 0, ["Outdoorsy", "Romantic"]),
    ("Fabrica", "Café", "Zamalek", 140, 0, ["Chill & Quiet", "Aesthetic / Instagrammable"]),
    ("El Dahan", "Restaurant", "Al-Hussein", 200, 1, ["Budget-Friendly", "Loud & Lively"]),
    ("來 (Lai)", "Restaurant", "New Cairo", 380, 1, ["Aesthetic / Instagrammable", "Romantic"]),
    ("Genaina Theater", "Entertainment", "Al-Azhar Park", 60, 1, ["Chill & Quiet", "Outdoorsy"]),
    ("Village Circle (VC)", "Entertainment", "Sheikh Zayed", 320, 0, ["Loud & Lively", "Late-Night"]),
]

REVIEW_SNIPPETS = [
    ("Sara M.", 5, "Exactly matched the vibe I was looking for, no surprises on price."),
    ("Omar K.", 4, "Good spot, a bit crowded on weekends but worth it."),
    ("Nourhan A.", 5, "Verified visit — prices were exactly as listed, no hidden fees."),
    ("Youssef T.", 3, "Decent, but service was slow during peak hours."),
    ("Mariam H.", 5, "Hidden gem honestly, glad the app surfaced this instead of the usual places."),
    ("Ahmed S.", 4, "Great for studying, quiet corner tables and good wifi."),
    ("Laila F.", 4, "Perfect budget match for our group outing."),
]


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def seed():
    conn = get_conn()
    with open("schema.sql") as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    cat_ids = {}
    for name, icon in CATEGORIES:
        cur.execute("INSERT INTO category (name, icon) VALUES (?, ?)", (name, icon))
        cat_ids[name] = cur.lastrowid

    vibe_ids = {}
    for name, icon in VIBES:
        cur.execute("INSERT INTO vibe (name, icon) VALUES (?, ?)", (name, icon))
        vibe_ids[name] = cur.lastrowid

    place_ids = []
    for name, cat, area, price, hidden, vibes in PLACES:
        cur.execute(
            """INSERT INTO place (name, description, category_id, area, price_per_person,
                                   image_url, is_hidden_gem, is_verified, lat, lng)
               VALUES (?, ?, ?, ?, ?, ?, ?, 1, ?, ?)""",
            (
                name,
                f"A {cat.lower()} in {area}, loved for its {vibes[0].lower()} atmosphere.",
                cat_ids[cat],
                area,
                price,
                None,
                hidden,
                30.0444 + random.uniform(-0.1, 0.1),
                31.2357 + random.uniform(-0.1, 0.1),
            ),
        )
        pid = cur.lastrowid
        place_ids.append(pid)
        for v in vibes:
            cur.execute(
                "INSERT INTO place_vibe (place_id, vibe_id) VALUES (?, ?)",
                (pid, vibe_ids[v]),
            )

        # 2-4 verified reviews per place
        for reviewer, rating, comment in random.sample(REVIEW_SNIPPETS, k=random.randint(2, 4)):
            cur.execute(
                """INSERT INTO review (place_id, reviewer_name, rating, comment, verified_visit)
                   VALUES (?, ?, ?, ?, 1)""",
                (pid, reviewer, rating, comment),
            )

    conn.commit()
    conn.close()
    print(f"Seeded {len(PLACES)} places, {len(CATEGORIES)} categories, {len(VIBES)} vibes.")


if __name__ == "__main__":
    seed()
