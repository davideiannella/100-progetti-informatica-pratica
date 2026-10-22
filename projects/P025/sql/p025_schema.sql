PRAGMA foreign_keys=ON;
CREATE TABLE patient(id INTEGER PRIMARY KEY, code TEXT UNIQUE NOT NULL);
CREATE TABLE doctor(id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE service(id INTEGER PRIMARY KEY, name TEXT NOT NULL, duration_min INTEGER NOT NULL CHECK(typeof(duration_min)='integer' AND duration_min>0));
CREATE TABLE slot(id INTEGER PRIMARY KEY, doctor_id INTEGER NOT NULL REFERENCES doctor(id),
                  service_id INTEGER NOT NULL REFERENCES service(id),
                  starts_at TEXT NOT NULL, UNIQUE(doctor_id, starts_at));
CREATE TABLE booking(id INTEGER PRIMARY KEY, patient_id INTEGER NOT NULL REFERENCES patient(id),
                     slot_id INTEGER NOT NULL UNIQUE REFERENCES slot(id), status TEXT NOT NULL DEFAULT 'BOOKED' CHECK(status='BOOKED'));
