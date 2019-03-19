[![Build Status](https://travis-ci.org/kodek-sleuth/FoodHub-Delivery-API.svg?branch=master)](https://travis-ci.org/kodek-sleuth/FoodHub-Delivery-API)
[![Coverage Status](https://coveralls.io/repos/github/kodek2000/Food-Hub-Backend/badge.svg?branch=master)](https://coveralls.io/github/kodek2000/Food-Hub-Backend?branch=master)

# **FOODHUB-DELIVERY API**
A Flask API that enables users make and have orders delivered to them.

## Project Dependencies
1. Python 3.6.7*
2. Postgresql 9.6.*
3. Flask 0.12.*

[Project Hosted on Heroku](https://foodhub-delivery.herokuapp.com/)

## Required Features
- Users can signUp for an account
- Users can Login to their account
- Users can view the menu of foods
- Users can order food on menu
- Users can choose food from a variety of restaurants
- Admins can confirm orders
- Admins can create new foods on menu
- Admins can delete foods on menu
- Admins can create restaurants
- admins can delete restaurants

## Endpoints
|  Method  |  Endpoint  |  Task  |
|  --- |  --- |  ---  |
|  `GET`  |  `/menu`  |  `Fetching Menu`  |
|  `POST`  |  `/auth/user/Register`  |  `Register a User`  |
|  `POST`  |  `/auth/user/Login`  |  `Login a User`  |
|  `POST`  |  `/auth/admin/Register`  |  `Register an Admin`  |
|  `POST`  |  `/auth/admin/Login`  |  `Login a User`  |
|  `POST`  |  `/menu`  |  `Add a Food to Menu`  |
|  `POST`  |  `/users/orders`  |  `Make an Order`  |
|  `GET`  |  `/user/Username/orders`  |  `Get order History of User`  |
|  `GET`  |  `/admin/users`  |  `Get all Users`  |
|  `POST`  |  `/auth/user/Register`  |  `Register a User`  |
|  `GET`  |  `/orders`  |  `Get all Orders`  |
|  `GET`  |  `/orders/<int>`  |  `Get Specific Order`  |
|  `PUT`  |  `/orders/<int>`  |  `Update Specific Order`  |
|  `DELETE`  |  `/orders/<int>`  |  `Delete Specific Order`  |
|  `GET`  |  `/restaurants`  |  `Get all Restaurants`  |
|  `POST`  |  `/restaurants`  |  `Add a Restaurant`  |
|  `DELETE`  |  `/restaurants/<int:restId>`  |  `Delete a Restaurant`  |
|  `POST`  |  `/admin/Logout`  |  `Logs Out a Admin`  |
|  `POST`  |  `/user/Logout`  |  `Logs Out a User`  |

## How to run flask application
1. Create a folder <foodhub-delivery> on your computer
   Clone repository to your computer into created folder

    ```
    git clone https://github.com/kodek2000/Food-Hub-Backend.git
    ```
2. Navigate into created folder

    ```
    cd  Food-Hub-Backend
    ```
3. Create and activate  virtual environment.

    ```
        $ virtualenv  venv

        $ source venv/bin/activate
    ```

    More on setting up Virtual environment: [how to set up virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

4. Install the packages in requirements.txt

    ``` pip3 install -r requirements.txt ```

5. Set up postgresql database and copy connection string for example.

    ``` DATABASE_URL='postgres://<db_user_name>:<password>@localhost/<database_name>' ```

    and

    ``` DATABASE_URL='postgres://<db_user_name>:<password>@localhost/<test_database_name>' ```

    How to setup postgresql: [how to setup postgresql mac](https://gist.github.com/sgnl/609557ebacd3378f3b72)

6. To start the api, using terminal, run the following commands

    ```export FLASK_APP='main_app.py'```

    ```export APP_SETTINGS='development'```

    ```export USER_SECRET_KEY='its nolonger a secret'```
     
    ```export ADMIN_SECRET_KEY='secret'```


    ```export DATABASE_URL='postgres://<db_user_name>:<password>@localhost/<database_name>'```

    ```export TEST_DB_URL='postgres://<db_user_name>:<password>@localhost/<test_database_name>```

    ```flask run ```

7. Using postman, the url to run the api locally is ```http://127.0.0.1:3000/```.

8. On the web, visit the url ```https://foodhub-delivery.herokuapp.com/apidocs/```

9. Using postman with web url ```https://foodhub-delivery.herokuapp.com/```

    
10.Sample: Use postman to navigate the endpoints in the api.

#### Authors
- Mugerwa Joseph Lumu


* **Ibrahim Mbaziira** - *Inspired By* - [code-sleuth](https://github.com/code-sleuth)

* **Mugerwa Joseph Lumu** - *Initial work* - [kodek2000](https://github.com/kodek2000)
