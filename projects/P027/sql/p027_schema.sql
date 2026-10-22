PRAGMA foreign_keys=ON;
CREATE TABLE member(id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE membership(id INTEGER PRIMARY KEY, member_id INTEGER NOT NULL REFERENCES member(id),
                        starts_on TEXT NOT NULL, ends_on TEXT NOT NULL, CHECK(ends_on>=starts_on));
CREATE TABLE class(id INTEGER PRIMARY KEY, name TEXT NOT NULL, capacity INTEGER NOT NULL CHECK(typeof(capacity)='integer' AND capacity>0));
CREATE TABLE attendance(member_id INTEGER NOT NULL REFERENCES member(id), class_id INTEGER NOT NULL REFERENCES class(id),
                        attended_on TEXT NOT NULL, PRIMARY KEY(member_id,class_id,attended_on));
