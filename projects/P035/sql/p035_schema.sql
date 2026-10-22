PRAGMA foreign_keys=ON;
CREATE TABLE account(id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL,
                     role TEXT NOT NULL CHECK(role IN ('reader','editor','admin')));
CREATE TABLE document(id INTEGER PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL);
CREATE TABLE audit_log(id INTEGER PRIMARY KEY, action TEXT NOT NULL,
                       document_id INTEGER, changed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TRIGGER audit_document_insert AFTER INSERT ON document
BEGIN INSERT INTO audit_log(action,document_id) VALUES ('INSERT',NEW.id); END;
CREATE TRIGGER audit_document_update AFTER UPDATE ON document
BEGIN INSERT INTO audit_log(action,document_id) VALUES ('UPDATE',NEW.id); END;
