import json
import pytest
import test_setup_testcase

class Admin_Resgister_Login_TestCase(test_setup_testcase.AuthTest):
    def test_Register_route(self):
        res=self.client().post('/auth/admin/Register', data=json.dumps(self.adminRegDetails), content_type='application/json')
        result=json.loads(res.data.decode())
        self.assertEqual(result["Message"], "You have successfully Created an Admin account")
        self.assertEqual(res.status, '201 CREATED')
    
    def test_Login_route(self):

        #Making That a admin that Registers successfully gets Logged in and gets Token
        request_Reg=self.client().post('/auth/admin/Register', data=json.dumps(self.adminRegDetails), content_type='application/json')
        result=json.loads(request_Reg.data.decode())
        self.assertEqual(result["Message"], "You have successfully Created an Admin account")
        self.assertEqual(request_Reg.status, '201 CREATED')

        #Making sure that Admin gets Logged In and Recieves Token
        request_Log=self.client().post('/auth/admin/Login', data=json.dumps(self.adminLogDetails), content_type='application/json')
        result=json.loads(request_Log.data.decode())
        self.assertEqual(result["Message"], "You have successfully Logged In")
        self.assertEqual(result["Access_Token"], result["Access_Token"])
        self.assertEqual(request_Log.status, '200 OK')
    
class Admin_Logout_TestCase(test_setup_testcase.AuthTest):
    def test_Logout_route(self):
         #Making That a admin that Registers successfully gets Logged in and gets Token
        request_Reg=self.client().post('/auth/admin/Register', data=json.dumps(self.adminRegDetails), content_type='application/json')
        result=json.loads(request_Reg.data.decode())
        self.assertEqual(result["Message"], "You have successfully Created an Admin account")
        self.assertEqual(request_Reg.status, '201 CREATED')

        #Making sure that Admin gets Logged In and Recieves Token
        request_Log_In=self.client().post('/auth/admin/Login', data=json.dumps(self.adminLogDetails), content_type='application/json')
        result=json.loads(request_Log_In.data.decode())
        self.assertEqual(result["Message"], "You have successfully Logged In")
        self.assertEqual(result["Access_Token"], result["Access_Token"])
        self.assertEqual(request_Log_In.status, '200 OK')

        #Making sure that Admin That Logs in can Logout
        request_Log_Out=self.client().post('/admin/Logout?token='+result["Access_Token"])
        result=json.loads(request_Log_Out.data.decode())
        self.assertEqual(result["Message"], "You have successfully Logged Out")
        self.assertEqual(result["Access_Token"], "Access Token has been Blacklisted")
        self.assertEqual(request_Log_Out.status, '200 OK')
    





       
        
        
