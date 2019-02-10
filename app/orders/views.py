import json
from app import *
from app.Models import *
from app.auth.user_auth.utilis import user_Required
from app.auth.admin_auth.utilis import admin_Required
from flask import Blueprint, Flask, jsonify, make_response, request

orders = Blueprint('orders', __name__)

@orders.route("/user/<string:Username>/orders", methods=['GET'])
@user_Required
def getOrderHistory(Username):
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

@orders.route("/user/orders/<string:Username>", methods=['POST'])
@user_Required
def makeOrder(Username):
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
            return make_response(jsonify(response)), 200
        
        except:
            response={
                    "Message":"Failed To make Order"
                }
            return make_response(jsonify(response)), 401



@orders.route("/orders", methods=['GET'])
@admin_Required
def getallOrders():
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
        return make_response(jsonify(request_orders)), 201

@orders.route("/orders/<int:orderId>", methods=['GET'])
@admin_Required
def getSpecificOrder(orderId):
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


@orders.route("/orders/<int:orderId>", methods=['PUT'])
@admin_Required
def upDateOrderStatus(orderId):
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

@orders.route("/orders/<int:orderId>", methods=['DELETE'])
@admin_Required
def deleteOrder(orderId):
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
