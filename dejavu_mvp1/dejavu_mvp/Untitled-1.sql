   
"""cursor.executescript("""
-- Déjà Vu — Smart Outing Recommendation Platform
-- Schema: places, categories, vibes, reviews, users, swipe rooms

DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS place_vibe;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS vibe;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS room_member;
DROP TABLE IF EXISTS room_swipe;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    icon TEXT NOT NULL DEFAULT '📍'
);

CREATE TABLE vibe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    icon TEXT NOT NULL DEFAULT '✨'
);

CREATE TABLE place (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    area TEXT NOT NULL,               -- Cairo neighborhood, e.g. "Zamalek"
    price_per_person INTEGER NOT NULL, -- EGP, avg spend per person
    image_url TEXT,
    is_hidden_gem INTEGER DEFAULT 0,   -- flag for "hidden gems" discovery cluster
    is_verified INTEGER DEFAULT 1,     -- verified partner (business partnership cluster)
    lat REAL,
    lng REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES category (id)
);

CREATE TABLE place_vibe (
    place_id INTEGER NOT NULL,
    vibe_id INTEGER NOT NULL,
    PRIMARY KEY (place_id, vibe_id),
    FOREIGN KEY (place_id) REFERENCES place (id) ON DELETE CASCADE,
    FOREIGN KEY (vibe_id) REFERENCES vibe (id) ON DELETE CASCADE
);

-- Verified-visit reviews: rating requires a "visit confirmation" flag,
-- reflecting the "Verified-Visit Reviews" idea (GPS/receipt check simulated by a checkbox at MVP stage)
CREATE TABLE review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_id INTEGER NOT NULL,
    reviewer_name TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    verified_visit INTEGER DEFAULT 1,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (place_id) REFERENCES place (id) ON DELETE CASCADE
);

-- Group Swipe-to-Match rooms (the highest-scoring idea, 8/9)
CREATE TABLE room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,          -- short shareable room code
    host_name TEXT NOT NULL,
    budget_max INTEGER,
    category_id INTEGER,
    status TEXT NOT NULL DEFAULT 'open', -- open | matched | closed
    matched_place_id INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES category (id),
    FOREIGN KEY (matched_place_id) REFERENCES place (id)
);

CREATE TABLE room_member (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    member_name TEXT NOT NULL,
    joined_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES room (id) ON DELETE CASCADE
);

CREATE TABLE room_swipe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    member_name TEXT NOT NULL,
    place_id INTEGER NOT NULL,
    liked INTEGER NOT NULL, -- 1 = like/right swipe, 0 = pass/left swipe
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES room (id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES place (id) ON DELETE CASCADE,
    UNIQUE (room_id, member_name, place_id)
);
)"""