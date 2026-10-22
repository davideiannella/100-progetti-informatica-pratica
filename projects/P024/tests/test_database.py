import unittest,sqlite3
from pathlib import Path
class T(unittest.TestCase):
 def setUp(self):
  base=Path(__file__).resolve().parents[1]; self.c=sqlite3.connect(':memory:'); self.c.execute('PRAGMA foreign_keys=ON'); self.c.executescript((base/'sql'/'schema.sql').read_text()); self.c.executescript((base/'sql'/'seed.sql').read_text())
 def tearDown(self): self.c.close()
 def test_counts(self): self.assertEqual(self.c.execute('select count(*) from Impresa').fetchone()[0],4)
 def test_join(self): self.assertEqual(self.c.execute("select p.Nome from Impresa i join Comune c on c.CodiceComune=i.CodiceComune join Provincia p on p.CodiceProvincia=c.CodiceProvincia where i.CodiceFiscale='I001'").fetchone()[0],'Latina')
 def test_fk(self):
  with self.assertRaises(sqlite3.IntegrityError): self.c.execute("insert into Impresa values('X','X',NULL,NULL,'999')")
 def test_unique_province(self):
  with self.assertRaises(sqlite3.IntegrityError): self.c.execute("insert into Provincia values('XX','Latina')")
if __name__=='__main__':unittest.main()
