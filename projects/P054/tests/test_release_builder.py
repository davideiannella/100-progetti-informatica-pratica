import json, hashlib, unittest
from pathlib import Path
import sys, zipfile
sys.path.append(str(Path(__file__).resolve().parents[1] / 'tools'))
from build_release import build

class ReleaseBuilderTest(unittest.TestCase):
    def test_build_creates_artifact_and_manifest(self):
        m=build(); root=Path(__file__).resolve().parents[1]
        artifact=root/'output'/m['artifact']
        self.assertTrue(artifact.exists())
        self.assertTrue((root/'output'/'release_manifest.json').exists())
        self.assertEqual(hashlib.sha256(artifact.read_bytes()).hexdigest(),m['sha256'])
    def test_zip_contains_application(self):
        m=build(); root=Path(__file__).resolve().parents[1]
        with zipfile.ZipFile(root/'output'/m['artifact']) as z:
            self.assertIn('src/app.py',z.namelist())
    def test_reproducible_artifact(self):
        a=build()['sha256']; b=build()['sha256']
        self.assertEqual(a,b)

if __name__=='__main__': unittest.main()
