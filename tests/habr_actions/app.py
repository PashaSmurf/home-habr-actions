import unittest
import json
from habr_actions import app as tested_app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'CHECK!!!!!')

    def test_post_hello_endpoint(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

    def test_get_api_endpoint(self):
        response = self.app.get('/api')
        self.assertEqual(response.json, {'status': 'test'})

    def test_correct_post_api_endpoint(self):
        response = self.app.post('/api',
                                 content_type='application/json',
                                 data=json.dumps({'name': 'Den', 'age': 100}))
        self.assertEqual(response.json, {'status': 'OK'})
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/api',
                                 content_type='application/json',
                                 data=json.dumps({'name': 'Den'}))
        self.assertEqual(response.json, {'status': 'OK'})
        self.assertEqual(response.status_code, 200)

    def test_not_dict_post_api_endpoint(self):
        response = self.app.post('/api',
                                 content_type='application/json',
                                 data=json.dumps([{'name': 'Den'}]))
        self.assertEqual(response.json, {'status': 'bad input'})
        self.assertEqual(response.status_code, 400)

    def test_no_name_post_api_endpoint(self):
        response = self.app.post('/api',
                                 content_type='application/json',
                                 data=json.dumps({'age': 100}))
        self.assertEqual(response.json, {'status': 'bad input'})
        self.assertEqual(response.status_code, 400)

    def test_bad_age_post_api_endpoint(self):
        response = self.app.post('/api',
                                 content_type='application/json',
                                 data=json.dumps({'name': 'Den', 'age': '100'}))
        self.assertEqual(response.json, {'status': 'bad input'})
        self.assertEqual(response.status_code, 400)
