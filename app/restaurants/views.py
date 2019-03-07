import json
from app import *
from app.Models import *
from flask.views import MethodView
from app.auth.user_auth.utilis import user_Required
from app.auth.admin_auth.utilis import admin_Required
from flask import Blueprint, Flask, jsonify, make_response, request

restaurant = Blueprint('restaurant', __name__)


class Get_Restaurants(MethodView):
    @swag_from('apidocs/get_all_restaurants.yaml', methods=['GET'])
    def get(self):
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


class Add_Restaurant(MethodView):
    decorators=[admin_Required]
    @swag_from('apidocs/add_restaurant.yaml', methods=['POST'])
    def post(self):
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
                    "Message":"You have Successfully Added Restaurant"
                    }
                return make_response(jsonify(response)), 201
            
            except:
                response={
                    "Message":"Failed To Add Restaurant"
                    }
                return make_response(jsonify(response)), 404


class Delete_Restaurant(MethodView):
    decorators=[admin_Required]
    @swag_from('apidocs/delete_a_restaurant.yaml', methods=['DELETE'])
    def delete(self, restId):
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

get_restaurants=Get_Restaurants.as_view('get_restaurants')
add_restaurant=Add_Restaurant.as_view('add_restaurant')
delete_restaurant=Delete_Restaurant.as_view('delete_restaurant')

restaurant.add_url_rule("/restaurants", view_func=get_restaurants, methods=['GET'])
restaurant.add_url_rule("/restaurants", view_func=add_restaurant, methods=['POST'])
restaurant.add_url_rule("/restaurants/<int:restId>", view_func=delete_restaurant, methods=['DELETE']) 