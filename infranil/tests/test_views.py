import unittest
from django.test.client import Client
from infranil.views import clean_path


class HelperTests(unittest.TestCase):
    def test_clean_path(self):
        test_cases = [
            ('/foo/', 'foo'),
            ('/foo/bar/', 'foo/bar'),
            ('foo/bar', 'foo/bar'),
            ('foo_bar', 'foo_bar'),
            ('foo-bar', 'foo-bar'),
            ('foo-----bar', 'foo-----bar'),
            ('../../etc/passwd', 'etc/passwd'),
            ('/etc/passwd', 'etc/passwd'),
        ]
        for (p, e) in test_cases:
            self.assertEqual(clean_path(p), e)


class ViewTest(unittest.TestCase):
    def setUp(self):
        self.c = Client()

    def test_valid_pages(self):
        test_cases = [
            ("/infranil/a/", "infranil/test/a.html"),
            ("/infranil/a", "infranil/test/a.html"),
            ("/infranil/b/", "infranil/test/b.html"),
            ("/infranil/c/", "infranil/test/c.html"),
            ("/infranil/sub_dir/", "infranil/test/sub_dir/index.html"),
            ("/infranil/sub_dir/a", "infranil/test/sub_dir/a.html"),
            ("/infranil/sub_dir/b/", "infranil/test/sub_dir/b.html"),
            ("/infranil/sub_dir/c", "infranil/test/sub_dir/c.html"),
        ]
        for path, content in test_cases:
            r = self.c.get(path)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.content.strip(), content)

    def test_404(self):
        r = self.c.get("/infranil/nonexistant/")
        self.assertEqual(r.status_code, 404)
