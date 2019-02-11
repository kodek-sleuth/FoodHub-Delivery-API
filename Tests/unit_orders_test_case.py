import json
from Tests import unit_setup_testcase

class all_orders_test_case(unit_setup_testcase.AuthTest):

    #Making sure That an admin that Registers successfully gets Logged in and gets Token
    def test_view_all_orders_route(self):
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

        #Making sure that Admin That Logs in can view All Orders
        request_Log_Out=self.client().get('/orders?token='+result["Access_Token"])
        result=json.loads(request_Log_Out.data.decode())
        self.assertEqual(request_Log_Out.status, '200 OK')

    def get_order_history_of_user(self):
        #Making That a user that Registers successfully gets Logged in and gets Token
        request_Reg=self.client().post('/auth/user/Register', data=json.dumps(self.userRegDetails), content_type='application/json')
        result=json.loads(request_Reg.data.decode())
        self.assertEqual(result["Message"], "You have successfully Created a User account")
        self.assertEqual(request_Reg.status, '201 CREATED')

        #Making sure that user gets Logged In and Recieves Token
        request_Log_In=self.client().post('/auth/user/Login', data=json.dumps(self.userLogDetails), content_type='application/json')
        result=json.loads(request_Log_In.data.decode())
        self.assertEqual(result["Message"], "You have successfully Logged In")
        self.assertEqual(result["Access_Token"], result["Access_Token"])
        self.assertEqual(request_Log_In.status, '200 OK')

        #Making sure that user That Authorized User that Logs in can view History
        request_Log_Out=self.client().get('/user/userTest/orders?token='+result["Access_Token"])
        result=json.loads(request_Log_Out.data.decode())
        self.assertEqual(request_Log_Out.status, '200 OK')

    def making_order(self):
        
        #Making That a user that Registers successfully gets Logged in and gets Token
        request_Reg=self.client().post('/auth/user/Register', data=json.dumps(self.userRegDetails), content_type='application/json')
        result=json.loads(request_Reg.data.decode())
        self.assertEqual(result["Message"], "You have successfully Created a User account")
        self.assertEqual(request_Reg.status, '201 CREATED')

        #Making sure that user gets Logged In and Recieves Token
        request_Log_In=self.client().post('/auth/user/Login', data=json.dumps(self.userLogDetails), content_type='application/json')
        result=json.loads(request_Log_In.data.decode())
        self.assertEqual(result["Message"], "You have successfully Logged In")
        self.assertEqual(result["Access_Token"], result["Access_Token"])
        self.assertEqual(request_Log_In.status, '200 OK')

        #Making sure that user That Authorized User that Logs in can make an Order
        request_make_Order=self.client().post('/user/userTest/orders?token='+result["Access_Token"], data=json.dumps(self.makeOrder), content_type='application/json')
        result=json.loads(request_make_Order.data.decode())
        self.assertEqual(result["Message"], "You have successfully made your order.")
        self.assertEqual(request_make_Order.status, '201 CREATED')
    
    def get_Specific_Order(self):

        #
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


        #Making sure that user That Authorized User that Logs in can get a specific Order
        request_get_Order=self.client().get('/orders/1?token='+result["Access_Token"], data=json.dumps(self.makeOrder), content_type='application/json')
        result=json.loads(request_make_Order.data.decode())
        self.assertEqual(result["Order"], result["Order"])
        self.assertEqual(request_make_Order.status, '200 OK')




