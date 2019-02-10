import json
from Tests import unit_setup_TestCase

class AdminResgisterTest(unit_setup_TestCase.AuthTest):
    def test_Register_route(self):
        res=self.client().post('/auth/admin/Register', data=json.dumps(self.adminRegDetails), content_type='application/json')
        result=json.loads(res.data.decode())
        self.assertEqual(result["Message"], "You have successfully Created an Admin account")
        self.assertEqual(res.status, '201 CREATED')
       
        
        
