import unittest
from unit_setUpTestCase import *

class AdminResgisterTest(BaseTest):
    def test_Register_route(self):
        request_sent=self.client().post('/auth/admin/Register', data=json.dumps(self.adminRegDetails), content_type='application/json')
        response=json.loads(request_sent.data.decode())
        self.assertEqual(response["Message"], "You have successfully Created an Admin account")
    