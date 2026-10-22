PRAGMA foreign_keys=ON;
CREATE TABLE book(id INTEGER PRIMARY KEY, title TEXT NOT NULL);
CREATE TABLE member(id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE loan(id INTEGER PRIMARY KEY, book_id INTEGER NOT NULL REFERENCES book(id), member_id INTEGER NOT NULL REFERENCES member(id),
                  borrowed_on TEXT NOT NULL, due_on TEXT NOT NULL, returned_on TEXT);
CREATE VIEW active_loans AS SELECT * FROM loan WHERE returned_on IS NULL;
CREATE TRIGGER valid_due BEFORE INSERT ON loan
WHEN NEW.due_on < NEW.borrowed_on
BEGIN SELECT RAISE(ABORT,'due date before borrowed date'); END;

CREATE TRIGGER valid_due_update BEFORE UPDATE ON loan
WHEN NEW.due_on < NEW.borrowed_on
BEGIN SELECT RAISE(ABORT,'due date before borrowed date'); END;
CREATE UNIQUE INDEX one_active_loan ON loan(book_id)
WHERE returned_on IS NULL;
