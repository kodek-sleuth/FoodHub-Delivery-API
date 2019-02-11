import json
from app import *
from app.Models import *
from flask.views import MethodView
from flask import current_app, Blueprint
from app.auth.user_auth.utilis import user_Required

user_auth=Blueprint('user_auth', __name__)

#Creating Class based views for Registration, Login and Logout as well as The Token
class RegistrationView(MethodView):
    def post(self):
        try:
            request_data = request.get_json(force=True)
            name=request_data["Name"]
            username=request_data["Username"]
            email=request_data["Email"]
            password=request_data["Password"]
            country=request_data["Country"]
            city=request_data["City"]
            address=request_data["Address"]
            try:
                user=User.query.filter(Username=username).first()
                if user.Username==username:
                    response={
                        "Message":"An account already exists with that Username"
                    }
                    return make_response(jsonify(response)), 409

            except:
                if '~!@#$%&*():;+=-/' in username:
                    response={
                        "Message":"Username can only have Letters and numbers at the end"
                    }
                    
                    return make_response(jsonify(response)), 401

                else:
                    userReg=User.addUser(name, email, username, password, country, city, address)
                    response={
                        "Message":"You have successfully Created a User account"
                    }
                    return make_response(jsonify(response)), 201
    
        except:
            response={
                "Message":"Please Enter valid Credentials"
            }
            return make_response(jsonify(response)), 409

class LoginView(MethodView):
    def post(self):
        try:
            request_data = request.get_json(force=True)
            user=User.query.filter_by(Username=request_data["Username"]).first()
            if user.Username==request_data["Username"] and user.Password==request_data["Password"]:
                expiration_time=datetime.datetime.utcnow()+datetime.timedelta(hours=1)
                token=jwt.encode({'exp':expiration_time}, current_app.config['USER_SECRET_KEY'], algorithm='HS256')
                response={
                    "Message":"You have successfully Logged In",
                    "Access_Token":token.decode('utf-8')
                }
                
                return make_response(jsonify(response)), 200
        
        except:
            response={
                "Message":"Try checking Your Credentials and Try again"
            }
            return make_response(jsonify(response)), 401

class LogOutView(MethodView):
    decorators=[user_Required]
    def post(self):
        try:
            token=request.args.get('token')
            tokenToDB=BlacklistToken.saveToken(token)
            response={
                    "Message":"You have successfully Logged Out",
                    "Access_Token":"Access Token has been Blacklisted"
                }
                
            return make_response(jsonify(response)), 200
        
        except:
            response={
                    "Message":"LogOut attempt failed try again"
                }
                
            return make_response(jsonify(response)), 401

#Creating View Function/Resources
registrationview=RegistrationView.as_view('registrationview')
loginview=LoginView.as_view('loginview')
logoutview=LogOutView.as_view('logoutview')

#adding routes to the Views we just created
user_auth.add_url_rule('/auth/user/Register', view_func=registrationview, methods=['POST'])
user_auth.add_url_rule('/auth/user/Login', view_func=loginview, methods=['POST'])
user_auth.add_url_rule('/user/Logout', view_func=logoutview, methods=['POST'])