from app import app
import unittest

class AppTest(unittest.TestCase):
    def test_world(self):
        client = app.test_client()
        self.assertIn('Hello World', client.get('/').data)

if __name__ == '__main__':
    unittest.main()
