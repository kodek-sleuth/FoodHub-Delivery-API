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
            request_data = request.get_json()
            userReg=User.addUser(request_data["Name"], request_data["Email"], request_data["Username"], request_data["Password"], request_data["Country"], request_data["City"], request_data["Address"])
            response={
                "Message":"You have successfully Created, Please Login"
            }
            return make_response(jsonify(response)), 200
        
        except:
            response={
                "Message":"Try checking Your Credentials and Try again"
            }
            return make_response(jsonify(response)), 401

class LoginView(MethodView):
    def post(self):
        try:
            request_data = request.get_json()
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
                    "Message":"You have successfully Logged Out"
                }
            
            return make_response(jsonify(response))
        
        except:
            response={
                    "Message":"You either not Logged In or have an Invalid Token"
                }
            
            return make_response(jsonify(response))

        

#Creating View Function/Resources
registrationview=RegistrationView.as_view('registrationview')
loginview=LoginView.as_view('loginview')
logoutview=LogOutView.as_view('logoutview')

#adding routes to the Views we just created
user_auth.add_url_rule('/auth/user/Register', view_func=registrationview, methods=['POST'])
user_auth.add_url_rule('/auth/user/Login', view_func=loginview, methods=['POST'])
user_auth.add_url_rule('/user/LogOut', view_func=logoutview, methods=['POST'])