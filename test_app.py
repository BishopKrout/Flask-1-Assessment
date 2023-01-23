import unittest
from flask import Flask, request
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = app.test_client()

    def test_home_route(self):
        # Send a GET request to the home route
        response = self.client.get("/")
        # Assert that the response has a 200 status code
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the correct template
        self.assertIn(b"home.html", response.data)
        
    def test_convert_route(self):
        # Send a POST request to the convert route with test data
        response = self.client.post("/", data={"amount": "10", "from_currency": "USD", "to_currency": "USD"})
        # Assert that the response has a 200 status code
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the correct amount
        self.assertIn(b"10", response.data)
        # Assert that the response contains the correct from_currency
        self.assertIn(b"USD", response.data)
        # Assert that the response contains the correct to_currency
        self.assertIn(b"USD", response.data)
        # Assert that the response contains the correct converted_amount
        self.assertIn(b"converted_amount", response.data)
        # Assert that the response contains the correct from_symbol
        # self.assertIn(b"from_symbol", response.data)
        # # Assert that the response contains the correct to_symbol
        # self.assertIn(b"to_symbol", response.data)

if __name__ == '__main__':
    unittest.main()