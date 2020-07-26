import unittest

from .. services.ContactService import ContactService


######
# Tests incomplets...
######

class TestApi(unittest.TestCase):

    def setUp(self):
        app = ContactService.get_all_contact()
        self.response = app.get('/')

    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    
    def test_object_response(self):
        self.assertEqual(Object, self.response.data.decode('utf-8'))

    
    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)
        

if __name__ == '__main__':
    unittest.main()