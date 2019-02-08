import json
from app import *
from app.Models import *
from app.auth.user_auth.utilis import user_Required
from app.auth.admin_auth.utilis import admin_Required
from flask import Blueprint, Flask, jsonify, make_response, request

restaurant = Blueprint('restaurant', __name__)

@restaurant.route("/restaurants", methods=['GET'])
def getRestaurants():
    try:
        restaurants=Restaurants.query.all()
        restaurantsToStr=str(restaurants)
        restaurantsToPy=json.loads(restaurantsToStr)
        return make_response(jsonify(restaurantsToPy)), 200
    
    except:
        response={
            "Message":"Failed To Get Restaurants"
            }
        return make_response(jsonify(response)), 404

@restaurant.route("/restaurants", methods=['POST'])
@admin_Required
def addRestaurant():
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
            request_data=request.get_json()
            restaurantToAdd=Restaurants.addRestaurant(request_data["Name"], request_data["Location"])
            response={
                "Message":"Successfully Added Restaurant."
                }
            return make_response(jsonify(response)), 201
        
        except:
            response={
                "Message":"Failed To Add Restaurant"
                }
            return make_response(jsonify(response)), 404

@restaurant.route("/restaurants/<int:restId>", methods=['DELETE'])
@admin_Required
def deleteRestaurant(restId):
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
            rest=Restaurants.query.filter_by(id=restId).delete()
            db.session.commit()
            response={
                "Message":"Successfully Deleted Restaurant"
            }
            return make_response(jsonify(response)), 200
        
        except:
            response={
                "Message":"Failed To Delete Restaurant"
                }
            return make_response(jsonify(response)), 404
