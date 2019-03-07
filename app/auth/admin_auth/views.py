import json
from app import *
from app.Models import *
from flask.views import MethodView
from flask import current_app, Blueprint
from app.auth.admin_auth.utilis import admin_Required

admin_auth=Blueprint('admin_auth', __name__)

#Creating Class based views for Registration, Login and Logout as well as The Token
class RegistrationView(MethodView):
    @swag_from('apidocs/register_admin.yaml', methods=['POST'])
    def post(self):
        try:
            request_data = request.get_json(force=True)
            username=request_data["Username"]
            email=request_data["Email"]
            password=request_data["Password"]
            name=request_data["Name"]
            try:
                admin=Admin.query.filter(Username=username).first()
                if admin.Username==username:
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
                    adminReg=Admin.create_admin(request_data["Name"], request_data["Email"], request_data["Username"], request_data["Password"])
                    response={
                        "Message":"You have successfully Created an Admin account"
                    }
                    return make_response(jsonify(response)), 201
    
        except:
            response={
                "Message":"Please Enter valid Username or Email"
            }
            return make_response(jsonify(response)), 409

class LoginView(MethodView):
    @swag_from('apidocs/login.yaml', methods=['POST'])
    def post(self):
        try:
            request_data = request.get_json(force=True)
            admin=Admin.query.filter_by(Username=request_data["Username"]).first()
            if admin.Username==request_data["Username"] and admin.Password==request_data["Password"]:
                expiration_time=datetime.datetime.utcnow()+datetime.timedelta(hours=24)
                token=jwt.encode({'exp':expiration_time}, current_app.config['ADMIN_SECRET_KEY'], algorithm='HS256')
                response={
                    "Message":"You have successfully Logged In",
                    "Access_Token":token.decode('utf-8')
                }
                
                return make_response(jsonify(response)), 200
        
        except:
            response={
                "Message":"Please Enter valid Username or Email"
            }
            return make_response(jsonify(response)), 401

class LogOutView(MethodView):
    decorators=[admin_Required]
    @swag_from('apidocs/logout.yaml', methods=['POST'])
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

class AllUsersView(MethodView):
    decorators=[admin_Required]
    def get(self):
        token=request.args.get('token')
        try:
            checkToken=BlacklistToken.query.filter_by(Token=token).first()
            if token==checkToken.Token:
                response={
                "Message":"You have an Expired Token, Login To get New Token."
                    }
                return make_response(jsonify(response)), 501
                
        except:
            try:
                user=Admin.viewAllUsers()
                userstr=str(user)
                usersToPy=json.loads(userstr)
                return make_response(jsonify(usersToPy)), 200
            
            except:
                response={
                    "Message":"Failed To Get Users"
                    }
                return make_response(jsonify(response)), 404


#Creating View Function/Resources
registrationview=RegistrationView.as_view('registrationview')
loginview=LoginView.as_view('loginview')
logoutview=LogOutView.as_view('logoutview')
allusersview=AllUsersView.as_view('allusersview')

#adding routes to the Views we just created
admin_auth.add_url_rule('/auth/admin/Register', view_func=registrationview, methods=['POST'])
admin_auth.add_url_rule('/auth/admin/Login', view_func=loginview, methods=['POST'])
admin_auth.add_url_rule('/admin/Logout', view_func=logoutview, methods=['POST'])
admin_auth.add_url_rule('/admin/users', view_func=allusersview, methods=['GET'])