import unittest
from main import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        resp = self.app.get('/')
        self.assertIn('Welcome', resp.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
