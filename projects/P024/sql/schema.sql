PRAGMA foreign_keys=ON;
CREATE TABLE Provincia(
  CodiceProvincia TEXT PRIMARY KEY NOT NULL,
  Nome TEXT NOT NULL UNIQUE
);
CREATE TABLE Comune(
  CodiceComune TEXT PRIMARY KEY NOT NULL,
  Nome TEXT NOT NULL,
  CodiceProvincia TEXT NOT NULL REFERENCES Provincia(CodiceProvincia)
);
CREATE TABLE Impresa(
  CodiceFiscale TEXT PRIMARY KEY NOT NULL,
  RagioneSociale TEXT NOT NULL,
  Indirizzo TEXT,
  CAP TEXT,
  CodiceComune TEXT NOT NULL REFERENCES Comune(CodiceComune)
);
