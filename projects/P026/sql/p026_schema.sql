PRAGMA foreign_keys=ON;
CREATE TABLE student(id INTEGER PRIMARY KEY, matricola TEXT UNIQUE NOT NULL, name TEXT NOT NULL);
CREATE TABLE course(id INTEGER PRIMARY KEY, code TEXT UNIQUE NOT NULL, title TEXT NOT NULL, credits INTEGER NOT NULL CHECK(typeof(credits)='integer' AND credits>0));
CREATE TABLE exam_session(id INTEGER PRIMARY KEY, course_id INTEGER NOT NULL REFERENCES course(id), exam_date TEXT NOT NULL);
CREATE TABLE registration(student_id INTEGER NOT NULL REFERENCES student(id), session_id INTEGER NOT NULL REFERENCES exam_session(id),
                          PRIMARY KEY(student_id,session_id));
CREATE TABLE result(student_id INTEGER NOT NULL, session_id INTEGER NOT NULL, grade INTEGER NOT NULL CHECK(typeof(grade)='integer' AND grade BETWEEN 18 AND 30),
                    honors INTEGER NOT NULL DEFAULT 0 CHECK(honors IN (0,1) AND (honors=0 OR grade=30)),
                    PRIMARY KEY(student_id,session_id),
                    FOREIGN KEY(student_id,session_id) REFERENCES registration(student_id,session_id));
