<p align="center">
  <img src="https://img.shields.io/badge/MVP-Functional%20Prototype-111827?style=for-the-badge" alt="Functional MVP">
  <img src="https://img.shields.io/badge/Python-Flask-111827?style=for-the-badge&logo=python&logoColor=white" alt="Python Flask">
  <img src="https://img.shields.io/badge/SQLite-Database-111827?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/JavaScript-Interactive%20UI-111827?style=for-the-badge&logo=javascript&logoColor=white" alt="JavaScript">
</p>

<h1 align="center">Déjà Vu</h1>

<p align="center">
  <strong>Smart outing discovery for people who don't know where to go.</strong>
</p>

<p align="center">
  <em>أروح فين؟ — Where do we go?</em>
</p>

<p align="center">
  Budget-first discovery · Group matching · Vibe-based filtering · Hidden gems · Reviews
</p>

<p align="center">
  <a href="mailto:amrahmadsalah@gmail.com">📧 Email</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/Amr-Ahmad-dev">💻 GitHub</a>
  &nbsp;•&nbsp;
  <a href="https://www.linkedin.com/in/amrahmadsalah">🔗 LinkedIn</a>
</p>

---

# ✦ The Idea

Choosing somewhere to go sounds simple.

For a group, it often isn't.

```text
"Where should we go?"
        ↓
"How much is it?"
        ↓
"Is it actually good?"
        ↓
"Does everyone want it?"
        ↓
"Is there somewhere better?"
        ↓
      ...
```

**Déjà Vu** was designed around a different idea:

> **Don't make people browse endlessly. Help them reach a decision.**

The MVP treats outing discovery as a combination of **constraints, preferences, and group consensus** rather than simply a directory of places.

---

# 🎯 The Problem

Students and young adults can lose a surprising amount of time deciding where to go, especially when several people are involved.

A useful outing decision often has to satisfy several conditions at once:

```text
                 ┌──────────────┐
                 │    BUDGET    │
                 │ What can we  │
                 │    afford?   │
                 └──────┬───────┘
                        │
                        ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│     VIBE     │  │    GROUP     │  │    TRUST     │
│ What kind of │  │ Who is going │  │ Can we trust │
│ experience?  │  │    with us?  │  │ the review?  │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       └──────────────────┼──────────────────┘
                          ▼
                 ┌────────────────┐
                 │   DECISION     │
                 │ Where should   │
                 │ we actually go?│
                 └────────────────┘
```

Déjà Vu is an MVP attempt to make that decision easier.

---

# 🚀 What I Built

The product combines several ideas into one decision-oriented flow.

| Feature | What it solves |
|---|---|
| 💰 **Budget-First Search** | Finds places within a user's spending limit |
| 👥 **Group Swipe-to-Match** | Finds places liked by everyone in a group |
| 🎭 **Vibe Filtering** | Searches by experience instead of only category |
| 💎 **Hidden Gem Discovery** | Gives lesser-known places additional visibility |
| ⭐ **Verified-Visit Reviews** | Distinguishes review confirmation from ordinary reviews |
| 🧮 **Group Cost Estimation** | Estimates expected cost for the whole group |

### The core loop

```text
DEFINE CONSTRAINTS
       │
       ├── Budget
       ├── Vibe
       ├── Category
       └── Group size
              │
              ▼
         DISCOVER PLACES
              │
              ▼
        SWIPE / EXPLORE
              │
              ▼
      EACH PERSON DECIDES
              │
              ▼
       FIND COMMON LIKES
              │
              ▼
          MATCHES
              │
              ▼
       MAKE A DECISION
```

The goal is not to maximize browsing.

It is to reduce **decision friction**.

---

# 🧭 Research → Product

Déjà Vu was developed from the **DÉJÀ VU × INNOVEGYPT** research and ideation process rather than from a random feature list.

```text
┌──────────────────────┐
│    USER RESEARCH     │
├──────────────────────┤
│ Problem identification│
│ Empathy maps         │
│ Personas             │
│ POV                  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      IDEATION        │
├──────────────────────┤
│ Business Model Canvas│
│ Feature ideas        │
│ Idea scoring         │
│ Feature clustering   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   PRIORITIZATION     │
├──────────────────────┤
│ Highest-value ideas  │
│ selected for MVP     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│         MVP          │
├──────────────────────┤
│ Budget-first search  │
│ Group matching       │
│ Vibe discovery       │
│ Hidden gems          │
└──────────────────────┘
```

### Ideation results

| Concept | Score | MVP status |
|---|:---:|---|
| **Group Swipe-to-Match** | **8/9** | ✅ Implemented |
| Reverse Budget-First Search | 7/9 | ✅ Implemented |
| Vibe & Mood Filtering | 7/9 | ✅ Implemented |
| Hidden Gem Discovery | — | ✅ Implemented |
| Verified-Visit Reviews | — | ✅ MVP implementation |

The important connection is:

**user problem → idea → priority → implementation**

---

# 💰 01 — Budget-First Discovery

Instead of making the user inspect places one by one and calculate affordability manually, the platform begins with a maximum spending amount per person.

```text
Maximum budget / person
          │
          ▼
┌─────────────────────────┐
│ Filter available places │
│ that fit the constraint  │
└────────────┬────────────┘
             │
             ▼
      Relevant options
```

The group estimate is then:

```text
Estimated outing cost
        =
Price per person × Group size
```

This puts the financial constraint at the beginning of the decision rather than after the user has already spent time exploring a place.

---

# 🎭 02 — Vibe & Mood Discovery

Traditional discovery systems often begin with categories such as restaurants, cafés, parks, or entertainment.

Déjà Vu adds another layer:

> **What kind of experience are you looking for?**

Examples include:

```text
┌──────────┐  ┌─────────────────┐  ┌────────────┐
│  Chill   │  │ Study-Friendly  │  │  Romantic  │
└──────────┘  └─────────────────┘  └────────────┘

┌──────────┐  ┌────────────┐
│  Social  │  │  Outdoor   │
└──────────┘  └────────────┘
```

The MVP contains **eight vibe-oriented tags**.

The idea is to move discovery closer to the way people naturally describe an outing:

> “I want somewhere chill.”

rather than requiring them to start with:

> “I want a café.”

---

# 🔎 03 — Place Discovery

The discovery layer combines multiple constraints instead of relying on a single category.

```text
                  ┌───────────┐
                  │  BUDGET   │
                  └─────┬─────┘
                        │
┌────────────┐          │          ┌────────────┐
│  CATEGORY  │──────────┼──────────│    VIBE    │
└────────────┘          │          └────────────┘
                        ▼
                ┌───────────────┐
                │    PLACES     │
                └───────┬───────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
      ┌───────────────┐   ┌───────────────┐
      │ Normal        │   │ Hidden Gem    │
      │ discovery     │   │ visibility    │
      └───────────────┘   └───────────────┘
```

The result is meant to be a more relevant set of options rather than another large directory.

---

# 👥 04 — Group Swipe-to-Match

This is the central interaction pattern of the MVP and the **highest-scoring idea from the original ideation process (8/9)**.

A group creates a room, shares its code, and each person independently evaluates places.

```text
                   GROUP ROOM
                ┌───────────────┐
                │    ABC123     │
                └───────┬───────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       PERSON A      PERSON B      PERSON C
          │             │             │
       Swipe         Swipe         Swipe
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                 SHARED DECISIONS
                        │
                        ▼
                 COMMON MATCHES
```

The conceptual matching operation is:

```text
Likes(A)
   ∩
Likes(B)
   ∩
Likes(C)
   ∩
  ...
   =
COMMON MATCHES
```

A place becomes a match when all current members of the room have liked it.

The product question therefore changes from:

> **“Where should we go?”**

into:

> **“Which places do we all agree on?”**

---

# ⭐ 05 — Reviews & Visit Confirmation

Reviews contain a `verified_visit` state.

For the MVP, this is deliberately a **confirmation mechanism**, not proof of physical presence.

```text
User submits review
        │
        ▼
┌──────────────────────┐
│ Visit confirmation   │
│ mechanism in the MVP │
└──────────┬───────────┘
           ▼
   verified_visit = true
```

### Important boundary

The MVP does **not** claim to provide strong real-world visit verification.

A production version could later strengthen this through:

```text
MVP confirmation
       │
       ▼
┌─────────────────────┐
│ Possible future     │
│ evidence sources    │
├─────────────────────┤
│ GPS                 │
│ Receipt             │
│ Booking             │
└─────────────────────┘
```

That distinction keeps the prototype honest about what it currently proves.

---

# 💎 06 — Hidden Gems

Déjà Vu includes a mechanism for identifying places as **hidden gems**.

Those places receive additional visibility in discovery.

```text
                     PLACES
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      Popular places       Hidden gems
             │                   │
             │            extra visibility
             │                   │
             └──────────┬────────┘
                        ▼
                    DISCOVERY
```

The intent is to reduce the tendency for discovery to repeatedly surface only the most obvious locations.

---

# 🗃️ Data Model

The application uses a relational **SQLite** database.

```text
                 ┌────────────────┐
                 │     PLACE      │
                 ├────────────────┤
                 │ id             │
                 │ name           │
                 │ category       │
                 │ area           │
                 │ price/person   │
                 │ hidden_gem     │
                 │ verified       │
                 └───────┬────────┘
                         │
                    many-to-many
                         │
                 ┌───────▼────────┐
                 │   PLACE_VIBE   │
                 └───────┬────────┘
                         │
                 ┌───────▼────────┐
                 │      VIBE      │
                 └────────────────┘

┌────────────────┐        ┌────────────────┐
│     REVIEW     │        │      ROOM      │
├────────────────┤        ├────────────────┤
│ rating         │        │ room code      │
│ comment        │        │ session        │
│ verified_visit │        └───────┬────────┘
└────────────────┘                │
                           ┌──────▼────────┐
                           │  ROOM_MEMBER   │
                           └──────┬────────┘
                                  │
                           ┌──────▼────────┐
                           │   ROOM_SWIPE  │
                           └───────────────┘
```

### Relationships

```text
Place ─────< PlaceVibe >───── Vibe

Room ──────< RoomMember

RoomMember ─────< RoomSwipe

Place ─────< Review
```

The many-to-many relationship between places and vibes is represented explicitly through `place_vibe`.

---

# 🏗️ Application Architecture

The MVP follows a straightforward server-rendered web architecture.

```text
┌──────────────────────────────────────────────────┐
│                    BROWSER                       │
│                                                  │
│       HTML · CSS · JavaScript · Jinja2          │
└───────────────────────┬──────────────────────────┘
                        │ HTTP
                        ▼
┌──────────────────────────────────────────────────┐
│                     FLASK                       │
│                                                  │
│ Routes → Request handling → Application logic   │
└───────────────────────┬──────────────────────────┘
                        │ SQL
                        ▼
┌──────────────────────────────────────────────────┐
│                    SQLITE                       │
│                                                  │
│ Places · Vibes · Reviews · Rooms · Swipes       │
└──────────────────────────────────────────────────┘
```

### Project structure

```text
dejavu/
│
├── app.py
│   └── Routes + application logic + DB queries
│
├── schema.sql
│   └── SQLite schema + relationships
│
├── seed.py
│   └── Database initialization + demo data
│
├── templates/
│   └── Jinja2 pages
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── swipe.js
│       └── main.js
│
├── requirements.txt
└── dejavu.db
```

### Main implementation files

| File | Responsibility |
|---|---|
| `app.py` | Routes, request handling, application logic, database queries |
| `schema.sql` | SQLite schema and relationships |
| `seed.py` | Database creation and demo-data population |
| `templates/` | Jinja2 server-rendered pages |
| `static/css/style.css` | Visual system and Cairo Dusk theme |
| `static/js/swipe.js` | Swipe cards, drag/tap interactions, match polling |
| `static/js/main.js` | Small client-side interactions such as flash-message dismissal |

---

# 🧰 Technology Stack

```text
                       DÉJÀ VU
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
      BACKEND          FRONTEND         DATABASE
         │                │                │
      Python             HTML             SQLite
      Flask              CSS
                         JavaScript
                         Jinja2
```

### Technologies used

- **Python**
- **Flask**
- **SQLite**
- **HTML**
- **CSS**
- **JavaScript**
- **Jinja2**

### Concepts demonstrated

- MVC-style application organization
- Relational database design
- SQL queries
- Many-to-many relationships
- Session-based group rooms
- Server-side rendering
- Form handling
- Filtering and search
- Recommendation logic
- Asynchronous match polling
- Client-side interaction
- Product-oriented MVP development

---

# 📊 Demo Dataset

The seed script creates a demonstration dataset representing:

```text
            25 CAIRO PLACES
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    Categories   Vibes      Pricing
        │          │          │
        └──────────┼──────────┘
                   ▼
              MVP DISCOVERY
```

The dataset makes the application testable without requiring an external live-place API.

---

# ▶️ Run Locally

## Requirements

- Python 3
- `pip`

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Initialize the database

```bash
python seed.py
```

This creates and populates:

```text
dejavu.db
```

## 3. Start the application

```bash
python app.py
```

## 4. Open it in your browser

```text
http://localhost:5000
```

---

# 🧪 Example User Journey

```text
┌──────────────┐
│     HOME     │
└──────┬───────┘
       ▼
┌──────────────┐
│ Set budget   │
└──────┬───────┘
       ▼
┌──────────────┐
│ Choose vibe  │
└──────┬───────┘
       ▼
┌──────────────┐
│   Discover   │
└──────┬───────┘
       ▼
┌──────────────┐
│ Create room  │
└──────┬───────┘
       ▼
┌──────────────┐
│ Share code   │
└──────┬───────┘
       ▼
┌──────────────────────────┐
│ Everyone swipes          │
│ independently            │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│ Common preferences       │
│ are identified            │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│        MATCHES            │
└────────────┬─────────────┘
             ▼
        Choose a place
```

The intended outcome is straightforward:

> **Less time deciding. More time actually going out.**

---

# 📦 MVP Scope

### Implemented

- [x] Budget-first search
- [x] Group swipe matching
- [x] Room codes
- [x] Vibe filtering
- [x] Hidden-gem discovery
- [x] Reviews
- [x] Verified-visit state
- [x] Group cost estimation
- [x] Cairo demo dataset
- [x] Responsive interactive UI

### Deliberately deferred

- [ ] Real user authentication
- [ ] GPS-based visit verification
- [ ] Receipt verification
- [ ] Payments
- [ ] Booking commissions
- [ ] Merchant dashboard
- [ ] Live chatbot assistant
- [ ] Production-grade live place data

These were intentionally kept outside the MVP so the core product hypothesis could be tested without prematurely building the surrounding commercial infrastructure.

---

# 🔭 Future Direction

```text
                         CURRENT MVP
                              │
                              ▼
                  ┌─────────────────────┐
                  │ Validate the core   │
                  │ recommendation      │
                  │ + group decision    │
                  └──────────┬──────────┘
                             │
                             ▼
                      REAL USER FEEDBACK
                             │
                             ▼
                   ┌────────────────────┐
                   │ Stronger product   │
                   │ + stronger data    │
                   └─────────┬──────────┘
                             │
               ┌─────────────┼─────────────┐
               ▼             ▼             ▼
          Accounts        Live data    Verification
               │             │             │
               └─────────────┼─────────────┘
                             ▼
                     Personalization
                             │
                             ▼
                    Booking integration
                             │
                             ▼
                      Merchant platform
```

Possible next steps:

- Real accounts and authentication
- GPS-based visit verification
- Receipt / booking verification
- Live place data
- Real-time availability
- Booking integration
- Merchant dashboard
- Personalized recommendation ranking
- Natural-language discovery
- Behavioral analytics
- Production deployment

---

# 🧠 Product Design Philosophy

The central product decision behind Déjà Vu is:

> **Start with the user's constraints, not the database's categories.**

A conventional discovery interface might begin with:

```text
Restaurants
Cafés
Parks
Entertainment
Shopping
```

Déjà Vu asks a different sequence:

```text
How much can we spend?
        ↓
What kind of experience do we want?
        ↓
Who are we going with?
        ↓
What do we all like?
        ↓
Where should we actually go?
```

That changes the role of the application.

It is not primarily trying to answer:

> **“What places exist?”**

It is trying to answer:

> **“Given our constraints and preferences, what should we choose?”**

---

# 🧩 MVP vs Production

One of the deliberate design choices in this project is separating **what is necessary to validate the idea** from **what is necessary to run a real commercial platform**.

```text
                  MVP
                   │
                   │ prove the core interaction
                   ▼
        ┌────────────────────────┐
        │ Recommendation        │
        │ + Group Matching       │
        └────────────┬───────────┘
                     │
                     ▼
              USER VALIDATION
                     │
                     ▼
                PRODUCTION
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
    Verification  Accounts    Live data
         │           │           │
         ▼           ▼           ▼
      Payments    Analytics   Booking
```

### Current status

> **MVP — Functional Prototype**

The application is functional and demonstrates the intended product flow, but it is **not presented as a production-ready commercial platform**.

Some systems are intentionally simplified or simulated because the purpose of this stage is to validate the core experience first.

---

# 💡 What This Project Demonstrates

Déjà Vu sits at the intersection of **software engineering and product thinking**.

```text
                    USER PROBLEM
                         │
                         ▼
                    USER RESEARCH
                         │
                         ▼
                       IDEATION
                         │
                         ▼
                    PRIORITIZATION
                         │
                         ▼
                         MVP
                         │
               ┌─────────┴─────────┐
               ▼                   ▼
        PRODUCT THINKING     SOFTWARE ENGINEERING
               │                   │
               ▼                   ▼
        User constraints      Flask application
        Group behavior        SQLite schema
        Feature priority      SQL queries
        User journey          JavaScript UI
               │                   │
               └─────────┬─────────┘
                         ▼
                 FUNCTIONAL PROTOTYPE
```

The project demonstrates experience with:

- Translating user research into software requirements
- Prioritizing features instead of building everything
- Designing an MVP around a specific problem
- Building a Flask web application
- Designing a relational SQLite database
- Implementing filtering and recommendation logic
- Implementing many-to-many relationships
- Building group decision workflows
- Creating interactive JavaScript components
- Rendering interfaces with Jinja2
- Designing a consistent visual system
- Separating MVP requirements from production requirements

More importantly, the project reinforces a broader engineering lesson:

> **Writing the code is only one part of building a product. Deciding what deserves to be built first is part of the engineering problem too.**

---

# 📍 Current Status

```text
┌────────────────────────────────────────────┐
│                 DÉJÀ VU                    │
│                                            │
│             FUNCTIONAL MVP                 │
│                                            │
│     Built for experimentation,             │
│     validation, and learning.              │
└────────────────────────────────────────────┘
```

**Built with:** Python · Flask · SQLite · Jinja2 · JavaScript · HTML · CSS

**Research:** DÉJÀ VU × INNOVEGYPT

**Dataset:** Cairo demonstration dataset

---

# 👋 About the Developer

<p align="center">
  <strong>Amr Ahmad</strong><br>
  Computer Science Student · Software & Product Development
</p>

<p align="center">
  Interested in building practical software where engineering, problem-solving,
  and product thinking meet.
</p>

<p align="center">
  <a href="mailto:amrahmadsalah@gmail.com">📧 Email</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="https://github.com/Amr-Ahmad-dev">💻 GitHub</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/amrahmadsalah">🔗 LinkedIn</a>
</p>

---

<p align="center">
  <strong>Déjà Vu</strong>
</p>

<p align="center">
  <em>Less scrolling. Less arguing. Better decisions.</em>
</p>

<p align="center">
  <strong>أروح فين؟</strong>
</p>

<p align="center">
  Smart outing discovery built around real constraints, real groups, and better decisions.
</p>

<p align="center">
  <a href="mailto:amrahmadsalah@gmail.com">Contact Amr</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/Amr-Ahmad-dev">View GitHub</a>
  &nbsp;•&nbsp;
  <a href="https://www.linkedin.com/in/amrahmadsalah">Connect on LinkedIn</a>
</p>

<p align="center">
  <sub>© 2026 Amr Ahmad · Déjà Vu MVP</sub>
</p>
