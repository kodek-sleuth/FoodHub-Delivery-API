import jwt
import datetime
from flask_cors import CORS
from flasgger import Swagger, swag_from
from flask_sqlalchemy import SQLAlchemy
from Settings.config import app_config
from flask import Flask, request, jsonify, make_response, redirect

db = SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config['SWAGGER'] = {
        'swagger': '2.0',
        'title': 'FoodHub Delivery-API',
        'description': "The innovative Food Hub api is an application that allows\
        users to order food on menu from a variety of dishes and from various restaurants and have it delivered at light speed.\
        \nThis is a RESTful API built in python using the Flask Framework.\
        \nGitHub Repository: 'https://github.com/kodek2000/Food-Hub-API'",
        'basePath': '/',
        'version': '0.1.0',
        'contact': {
            'Developer': 'Mugerwa Joseph Lumu',
            'email': 'mugerwalumu@gmail.com',
            'Company': 'None'
        },

        'schemes': [
            'http',
            'https'
        ],

        'license': {
            'name': 'MIT'
        },

        'tags': [
            {
                'name': 'User',
                'description': 'The basic unit of authentication'
            },
            {
                'name': 'Orders',
                'description': 'Enables a User To Place a food Order'
            },
            {
                'name': 'Restaurant',
                'description': 'A User can choose from here all types of food'
            },
            {
                'name': 'Token',
                'description': 'Authorisation to enable authentication of API'
            },
            
            {
                'name': 'Admin',
                'description': 'Overall user that moderates the API'
            },

            {
                'name': 'Menu',
                'description':'A list of Foods'
            }
        ],

        'specs_route': '/apidocs/'
    }

    
    db.init_app(app) 
    CORS(app)
    swagger=Swagger(app)

    @app.route('/')
    def index():
        return redirect('/apidocs/')

    
    from app.auth.admin_auth.views import admin_auth 
    from app.auth.user_auth.views import user_auth
    from app.orders.views import orders 
    from app.restaurants.views import restaurant
    from app.menu.views import menu

    app.register_blueprint(admin_auth)
    app.register_blueprint(user_auth)
    app.register_blueprint(orders)
    app.register_blueprint(restaurant)
    app.register_blueprint(menu)

    return app

    
