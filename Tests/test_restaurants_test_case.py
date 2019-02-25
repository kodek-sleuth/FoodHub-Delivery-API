import json
import test_setup_testcase

class viewRestaurants(test_setup_testcase.AuthTest):
    def test_all_restaurants(self):
        request_res=self.client().get('/restaurants')
        result=json.loads(request_res.data.decode())
        self.assertEqual(request_res.status, '200 OK')
    
class addRestuarant(test_setup_testcase.AuthTest):
    def test_admin_add_restaurant(self):
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

        #Making sure that admin can add a Restaurant
        request_res=self.client().post('/restaurants?token='+result["Access_Token"], data=json.dumps(self.add_restaurant), content_type='application/json')
        response=json.loads(request_res.data.decode())
        self.assertEqual(response["Message"], "You have Successfully Added Restaurant")
        self.assertEqual(request_res.status, '201 CREATED')

class delete_Restaurant(test_setup_testcase.AuthTest):
    def test_admin_delete_restaurant(self):
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

        #Making sure that admin can add a Restaurant
        request_res=self.client().post('/restaurants?token='+result["Access_Token"], data=json.dumps(self.add_restaurant), content_type='application/json')
        response=json.loads(request_res.data.decode())
        self.assertEqual(response["Message"], "You have Successfully Added Restaurant")
        self.assertEqual(request_res.status, '201 CREATED')

        #Making sure that admin deletes A Restaurant
        request_res=self.client().delete('/restaurants/1?token='+result["Access_Token"], data=json.dumps(self.add_restaurant), content_type='application/json')
        response=json.loads(request_res.data.decode())
        self.assertEqual(response["Message"], "Successfully Deleted Restaurant")
        self.assertEqual(request_res.status, '200 OK')




