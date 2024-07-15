import unittest
from app import app

class TestRecommendEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_recommend_endpoint(self):
        # Test with valid user_id
        response = self.app.post('/recommend', json={'user_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommendations', response.json)

    def test_invalid_request(self):
        # Test with missing user_id
        response = self.app.post('/recommend', content_type='application/json')
        self.assertEqual(response.status_code, 400)  # Expecting a bad request status code

        # Test with invalid user_id type
        response = self.app.post('/recommend', json={'user_id': 'invalid'}, content_type='application/json')
        self.assertEqual(response.status_code, 400)  # Expecting a bad request status code

        # Test with user_id as None
        response = self.app.post('/recommend', json={'user_id': None}, content_type='application/json')
        self.assertEqual(response.status_code, 400)  # Expecting a bad request status code

if __name__ == '__main__':
    unittest.main()
