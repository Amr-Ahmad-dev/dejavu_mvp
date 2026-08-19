# Déjà Vu — Smart Outing Recommendation Platform (MVP)

Built from the DÉJÀ VU × INNOVEGYPT research: problem statement, empathy maps,
persona work, POV, Business Model Canvas, and the ideation/scoring exercise.

Problem solved: **"أروح فين؟" ("Where do I go?")** — students and young adults
in Cairo waste time and money on outings because of unclear budgets, unreliable
reviews, and decision fatigue when planning with friends.

## What's implemented

Built directly from your ideation scores and clusters:

| Feature | Source | Notes |
|---|---|---|
| **Reverse Budget-First Search** | Idea #1 (7/9) | Set max spend per person, get matching places |
| **Group Swipe-to-Match** | Idea #2 (8/9, highest score) | Shareable room code, everyone swipes, auto-match when all agree |
| **Vibe & Mood filtering** | Idea #4 (7/9) | 8 vibe tags (Chill, Study-Friendly, Romantic, etc.) instead of just food categories |
| **Hidden gems surfacing** | Cluster 4, "Discovering the Widest Variety" | Flagged places get their own homepage section and priority in results |
| **Verified-visit reviews** | Idea #5 / Cluster 2 (Authenticity) | Reviews carry a "verified visit" flag; MVP simulates the check with a confirmation checkbox — a real GPS/receipt check is a v2 item |
| Budget × group size cost estimate | BMC "less distraction" value prop | Shown on the discover page |

## Stack

Flask + Jinja2 + SQLite (matches your Ledger project's stack), vanilla JS for
the swipe interaction (drag + tap), no frontend framework/build step needed.

## Run it

```bash
pip install -r requirements.txt
python seed.py      # creates dejavu.db and populates 25 Cairo places
python app.py        # http://localhost:5000
```

## Project structure

```
app.py              # all routes (MVC-style: routing + queries together, matches Ledger's app.py pattern)
schema.sql           # DB schema
seed.py               # demo data: 25 real-style Cairo places across 5 categories
templates/            # Jinja2 templates
static/css/style.css  # design system ("Cairo dusk" palette)
static/js/swipe.js    # swipe card drag/tap + match polling
static/js/main.js     # flash message dismiss
```

## Data model

- `place` — name, category, area, price/person, hidden-gem flag, verified flag
- `category` / `vibe` — lookup tables (categories from your BMC: Restaurant, Café, Park, Entertainment, Shopping)
- `place_vibe` — many-to-many
- `review` — rating, comment, `verified_visit` flag
- `room` / `room_member` / `room_swipe` — swipe-to-match sessions; a room matches when every current member has liked the same place

## What's deliberately out of scope for this MVP

- Real user accounts/auth (reviews are name-only for now)
- Real GPS/receipt verification (checkbox stand-in)
- Payments/commission handling (your BMC's revenue stream — booking/commission logic)
- Business/merchant dashboard (the B2B side of your BMC)
- Live chatbot assistant (from your flow diagram) — the filter form covers the same intent for MVP speed

These map to natural "next" milestones once the swipe-match core is validated with real users.
