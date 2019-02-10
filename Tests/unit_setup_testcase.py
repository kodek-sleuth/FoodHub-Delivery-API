import json
import unittest
from app import *

class AuthTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        with self.app.app_context():
            self.adminRegDetails = {
                "Name":"admin",
                "Email":"admintest@kitende.com",
                "Username":"adminT",
                "Password":"admintest"
            }

            self.adminLogDetails = {
                "Username":"adminTest",
                "Password":"admintest"
            }

            self.userRegDetails = {
                "Name":"adminTesting",
                "Email":"admin2Test.0@kitende.com",
                "Username":"adminTest",
                "Password":"admintest",
                "Country":"Canada",
                "City":"Ottawa",
                "Address":"Cronville"
            }

            self.userLogDetails = {
                "Username":"adminTest",
                "Password":"admintest"
            }

            self.makeOrder = {
                "Name":"Chips and Liver"
            }

            self.updateOrder = {
                "Name":"Processing"
            }

            self.addToMenu = {
                "Name":"Chips and Fish Salad",
                "Price":"Ugshs 12000"
            }

            db.session.close()
            db.drop_all()
            db.create_all()

            
