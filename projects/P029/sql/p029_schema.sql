PRAGMA foreign_keys=ON;
CREATE TABLE room(id INTEGER PRIMARY KEY, code TEXT UNIQUE NOT NULL);
CREATE TABLE booking(id INTEGER PRIMARY KEY, room_id INTEGER NOT NULL REFERENCES room(id),
                     start_date TEXT NOT NULL, end_date TEXT NOT NULL, CHECK(end_date>start_date));

CREATE TRIGGER no_overlap_insert BEFORE INSERT ON booking
WHEN EXISTS (SELECT 1 FROM booking b WHERE b.room_id=NEW.room_id
 AND NEW.start_date < b.end_date AND NEW.end_date > b.start_date)
BEGIN SELECT RAISE(ABORT,'overlapping booking'); END;
CREATE TRIGGER no_overlap_update BEFORE UPDATE ON booking
WHEN EXISTS (SELECT 1 FROM booking b WHERE b.id<>OLD.id
 AND b.room_id=NEW.room_id AND NEW.start_date < b.end_date
 AND NEW.end_date > b.start_date)
BEGIN SELECT RAISE(ABORT,'overlapping booking'); END;
