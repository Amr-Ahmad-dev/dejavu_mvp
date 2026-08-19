import sqlite3

with sqlite3.connect("dejavu.db") as conn:
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("insert into category (name, icon) values ('Restaurant', '🍽️')")
    cursor.execute("insert into category (name, icon) values ('Café', '☕')")
    cursor.execute("insert into category (name, icon) values ('Entertainment', '🎉')")
    cursor.execute("insert into category (name, icon) values ('Outdoor', '🏞️')")
    cursor.execute("insert into category (name, icon) values ('Shopping', '🛍️')")
    cursor.execute("insert into category (name, icon) values ('Cultural', '🏛️')")
    conn.commit()
    cursor.execute("insert into vibe (name, icon) values ('Romantic', '❤️')")
    cursor.execute("insert into vibe (name, icon) values ('Family-friendly', '�👨‍👩‍👧‍👦')")
    cursor.execute("insert into vibe (name, icon) values ('Trendy', '🔥')")
    cursor.execute("insert into vibe (name, icon) values ('Relaxed', '😌')")
    cursor.execute("insert into vibe (name, icon) values ('Adventurous', '🧗')")
    cursor.execute("insert into vibe (name, icon) values ('Cultural', '🎭')")
    conn.commit()
    cursor.execute("insert into place (name, description, category_id, area, price_per_person, image_url, is_hidden_gem, is_verified, lat, lng) values ('Zamalek Café', 'A cozy café in Zamalek.', 2, 'Zamalek', 15.0, NULL, 0, 1, 30.0626, 31.2195)")
    cursor.execute("insert into place (name, description, category_id, area, price_per_person, image_url, is_hidden_gem, is_verified, lat, lng) values ('Maadi Restaurant', 'A family-friendly restaurant in Maadi.', 1, 'Maadi', 25.0, NULL, 0, 1, 29.9722, 31.2765)") 
    cursor.execute("insert into place (name, description, category_id, area, price_per_person, image_url, is_hidden_gem, is_verified, lat, lng) values ('Heliopolis Entertainment Center', 'A trendy entertainment center in Heliopolis.', 3, 'Heliopolis', 30.0, NULL, 0, 1, 30.0985, 31.3346)")
    cursor.execute("insert into place (name, description, category_id, area, price_per_person, image_url, is_hidden_gem, is_verified, lat, lng) values ('Nasr City Park', 'A relaxed outdoor park in Nasr City.', 4, 'Nasr City', 0.0, NULL, 0, 1, 30.0561, 31.3406)")  
    cursor.execute("insert into place (name, description, category_id, area, price_per_person, image_url, is_hidden_gem, is_verified, lat, lng) values ('Downtown Shopping Mall', 'A shopping mall in Downtown.', 5, 'Downtown', 50.0, NULL, 0, 1, 30.0444, 31.2357)")  
    cursor.execute("insert into place (name, description, category_id, area, price_per_person, image_url, is_hidden_gem, is_verified, lat, lng) values ('Garden City Cultural Center', 'A cultural center in Garden City.', 6, 'Garden City', 20.0, NULL, 0, 1, 30.0459, 31.2243)") 
    conn.commit()
        









 