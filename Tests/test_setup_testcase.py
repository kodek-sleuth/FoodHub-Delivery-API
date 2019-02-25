import json
import unittest
from app import create_app, db

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
                "Username":"adminT",
                "Password":"admintest"
            }

            self.userRegDetails = {
                "Name":"userTesting",
                "Email":"user2Test.0@kitende.com",
                "Username":"userTest",
                "Password":"usertest",
                "Country":"Canada",
                "City":"Ottawa",
                "Address":"Cronville"
            }

            self.userLogDetails = {
                "Username":"userTest",
                "Password":"usertest"
            }

            self.make_order = {
                "Name":"Chips and Liver"
            }

            self.update_order_made = {
                "Status":"Processing"
            }

            self.add_restaurant={
                "Name":"Kentucky Fried Chicken",
                "Location":"Kampala"
            }

            self.addToMenu = {
                "Name":"Chips and Fish Salad",
                "Price":"Ugshs 12000"
            }

            db.session.close()
            db.drop_all()
            db.create_all()

            
