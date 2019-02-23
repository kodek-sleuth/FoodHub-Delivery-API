import json
from app import *
from app.Models import *
from flask.views import MethodView
from app.auth.user_auth.utilis import user_Required
from app.auth.admin_auth.utilis import admin_Required
from flask import Blueprint, Flask, jsonify, make_response, request

orders = Blueprint('orders', __name__)


class Get_History_Of_Orders(MethodView):
    decorators=[user_Required]
    @swag_from('apidocs/get_order_history.yaml', methods=['GET'])
    def get(self, Username):
        token=request.args.get('token')
        try:
            checkToken=BlacklistToken.query.filter_by(Token=token).first()
            if token==checkToken.Token:
                response={
                "Message":"You have an Expired Token, Login To get New Token."
                    }
                return make_response(jsonify(response)), 401
            
        except:
            history=User.viewOrderHistory(Username)
            historystr=str(history)
            historystrToPy=json.loads(historystr)
            return make_response(jsonify(historystrToPy)), 200


class Make_Order(MethodView):
    decorators=[user_Required]
    @swag_from('apidocs/making_order.yaml', methods=['POST'])
    def post(self, Username):
        token=request.args.get('token')
        try:
            checkToken=BlacklistToken.query.filter_by(Token=token).first()
            if token==checkToken.Token:
                response={
                "Message":"You have an Expired Token, Login To get New Token."
                    }
                return make_response(jsonify(response)), 401
        
        except:
            try:
                request_data = request.get_json(force=True)
                user = User.query.filter_by(Username=Username).first()
                order = Order.requestOrder(request_data["Name"], user.id)

                response={
                        "Message":"You have successfully made your order."
                    }
                return make_response(jsonify(response)), 201
            
            except:
                response={
                        "Message":"Failed To make Order"
                    }
                return make_response(jsonify(response)), 401


class Get_All_Orders(MethodView):
    decorators=[admin_Required]
    @swag_from('apidocs/get_all_orders.yaml', methods=['GET'])
    def get(self):
        token=request.args.get('token')
        try:
            checkToken=BlacklistToken.query.filter_by(Token=token).first()
            if token==checkToken.Token:
                response={
                "Message":"You have an Expired Token, Login To get New Token."
                    }
                return make_response(jsonify(response)), 401
        
        except:
            orders = Admin.placedOrders()
            ordersStr = str(orders)
            request_orders = json.loads(ordersStr)
            return make_response(jsonify(request_orders)), 200


class Get_Specific_Order(MethodView):
    decorators=[admin_Required]
    @swag_from('apidocs/get_specific_order.yaml', methods=['GET'])
    def get(self, orderId):
        token=request.args.get('token')
        try:
            checkToken=BlacklistToken.query.filter_by(Token=token).first()
            if token==checkToken.Token:
                response={
                "Message":"You have an Expired Token, Login To get New Token."
                    }
                return make_response(jsonify(response)), 401
        
        except:
            try:
                specificOrder = Admin.specificOrder(orderId)
                response={
                    "Order":specificOrder
                }
                return make_response(jsonify(response)), 200
            
            except:
                response={
                        "Message":"Failed To get Order"
                    }
                return make_response(jsonify(response)), 401


class Update_Order_Status(MethodView):
    decorators=[admin_Required]
    @swag_from('apidocs/update_order.yaml', methods=['PUT'])
    def put(self, orderId):
        token=request.args.get('token')
        try:
            checkToken=BlacklistToken.query.filter_by(Token=token).first()
            if token==checkToken.Token:
                response={
                "Message":"You have an Expired Token, Login To get New Token."
                    }
                return make_response(jsonify(response)), 401
        
        except:
            try:
                request_data = request.get_json()
                admin = Order.query.filter_by(id=orderId).first()
                admin.Status = request_data["Status"]
                db.session.commit()

                response={
                    "Message":"You have successfully Updated Order"
                }
                return make_response(jsonify(response)), 200
            
            except:
                response={
                    "Message":"Update Of Resource was unsuccessful"
                }
                return make_response(jsonify(response)), 401


class Delete_Order(MethodView):
    decorators=[admin_Required]
    @swag_from('apidocs/delete_an_order.yaml', methods=['DELETE'])
    def delete(self, orderId):
        token=request.args.get('token')
        try:
            checkToken=BlacklistToken.query.filter_by(Token=token).first()
            if token==checkToken.Token:
                response={
                "Message":"You have an Expired Token, Login To get New Token."
                    }
                return make_response(jsonify(response)), 401
        
        except:
            try:
                admin = Order.query.filter_by(id=orderId).delete()
                db.session.commit()

                response={
                    "Message":"You have successfully Deleted Order"
                }
                return make_response(jsonify(response)), 200
            
            except:
                response={
                    "Message":"Failed To Delete Resource"
                }
                return make_response(jsonify(response)), 401


get_history_of_orders=Get_History_Of_Orders.as_view('get_history_of_orders')

make_order=Make_Order.as_view('make_order')

get_all_orders=Get_All_Orders.as_view('get_all_orders')

get_specific_order=Get_Specific_Order.as_view('get_specific_order')

update_order_status=Update_Order_Status.as_view('update_order_status')

delete_order=Delete_Order.as_view('delete_order')


orders.add_url_rule('/user/<string:Username>/orders', view_func=get_history_of_orders, methods=['GET'])
orders.add_url_rule('/user/orders/<string:Username>', view_func=make_order, methods=['POST'])
orders.add_url_rule('/orders', view_func=get_all_orders, methods=['GET'])
orders.add_url_rule('/orders/<int:orderId>', view_func=get_specific_order, methods=['GET'])
orders.add_url_rule('/orders/<int:orderId>', view_func=update_order_status, methods=['PUT'])
orders.add_url_rule('/orders/<int:orderId>', view_func=delete_order, methods=['DELETE'])