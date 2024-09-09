import unittest
from app import create_app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b"Hello, Flask with Jenkins!", rv.data)

if __name__ == '__main__':
    unittest.main()
