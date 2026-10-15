import tempfile
import unittest
from pathlib import Path
from docforge import scan, render

class DocForgeTests(unittest.TestCase):
    def test_python_symbols(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "app.py").write_text("def greet():\n    pass\nclass Thing:\n    pass\n", encoding="utf-8")
            result = scan(root)
            self.assertEqual(result[0][0], "app.py")
            self.assertTrue(any("greet" in item for item in result[0][1]))
            self.assertIn("Project inventory", render("demo", result))

    def test_ignores_build_directories(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "node_modules").mkdir()
            (root / "node_modules" / "index.js").write_text("hello")
            self.assertEqual(scan(root), [])

if __name__ == "__main__":
    unittest.main()
