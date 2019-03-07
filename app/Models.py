import json
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), nullable=False, unique=True)
    Email = db.Column(db.String(30), nullable=False, unique=True)
    Username = db.Column(db.String(15), nullable=False, unique=True)
    Password = db.Column(db.String(200), nullable=False)
    Country = db.Column(db.String(20), nullable=False)
    City = db.Column(db.String(20), nullable=False)
    Address = db.Column(db.String(20), nullable=False)
    order = db.relationship('Order', lazy=True)

  
    def __init__(self, Name, Email, Username, Password, Country, City, Address):
        self.Name = Name
        self.Email = Email
        self.Username = Username
        self.Password = Password
        self.Country = Country
        self.City = City
        self.Address = Address
    
    def addUser(_Name, _Email, _Username, _Password, _Country, _City, _Address):
        addedUser = User(Name=_Name, Email=_Email, Username=_Username, Password=_Password, Country=_Country, City=_City, Address=_Address)
        db.session.add(addedUser)
        db.session.commit()
        
    def viewOrderHistory(_Username):
        allOrders = User.query.filter_by(Username=_Username).first()
        viewallOrders = allOrders.order
        return viewallOrders

    def __repr__(self):
        userObject = {
            "Username":self.Username,
            "Password":self.Password
        }
        
        return json.dumps(userObject)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Status = db.Column(db.String(200), default="New")
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, Name, User_id):
        self.Name = Name
        self.User_id = User_id
       
    def requestOrder(_Name, _User_id):
        placedOrder = Order(Name=_Name, User_id=_User_id)
        db.session.add(placedOrder)
        db.session.commit()

    def __repr__(self):
        orderObject = {
            "Name":self.Name,
            "Status":self.Status
        }
        return json.dumps(orderObject)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), nullable=False, unique=True)
    Email = db.Column(db.String(25), nullable=False, unique=True)
    Username = db.Column(db.String(15), nullable=False, unique=True)
    Password = db.Column(db.String(200), nullable=False)
   
    def __init__(self, Name, Email, Username, Password):
        self.Name = Name
        self.Email = Email
        self.Username = Username
        self.Password = Password
    
    def create_admin(_Name, _Email, _Username, _Password):
        addAdmin=Admin(Name=_Name, Email=_Email, Username=_Username, Password=_Password)
        db.session.add(addAdmin)
        db.session.commit()
    
    def removeUser(_Username):
        User.query.filter_by(Username=_Username).delete()
        db.session.commit()
    
    def viewAllUsers():
        users = User.query.all()
        return users
    
    def placedOrders():
        viewOrders = Order.query.all()
        return viewOrders
    
    def specificOrder(_id):
        orderAtMoment = Order.query.filter_by(id=_id).first()
        orderName = orderAtMoment.Name
        return orderName

    def addItemToMenu(_Name, _Price):
        menu1 = Menu(Name=_Name, Price=_Price)
        db.session.add(menu1)
        db.session.commit()
    
    def removeItemFromMenu(_Name):
        Menu.query.filter_by(Name=_Name).delete()
        db.session.commit()
    
    def getCurrentMenu():
        menu = Menu.query.all()
        return menu
    
    def __repr__(self):
        adminObject = {
            "Username":self.Username,
            "Password":self.Password
        }

        return json.dumps(adminObject)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Price = db.Column(db.String(200), nullable=False)

    def __init__(self, Name, Price):
        self.Name = Name
        self.Price = Price
     
    def __repr__(self):
        menuObject={
            "Name":self.Name,
            "Price":self.Price
        }
        return json.dumps(menuObject)

class BlacklistToken(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Token = db.Column(db.String(500), unique=True, nullable=False)

    def __init__(self, Token):
        self.Token = Token
    
    def saveToken(_Token):
        savedToken=BlacklistToken(Token=_Token)
        db.session.add(savedToken)
        db.session.commit()
    
    def __repr__(self):
        token_object={
            "Token":self.Token
        }

        return json.dumps(token_object)

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Location = db.Column(db.String(200), nullable=False)

    def __init__(self, Name, Location):
        self.Name=Name
        self.Location=Location
    
    def addRestaurant(_Name, _Location):
        addItem=Restaurants(Name=_Name, Location=_Location)
        db.session.add(addItem)
        db.session.commit()
    
    def __repr__(self):
        restaurantObject={
            "Name":self.Name,
            "Location":self.Location
        }
        return json.dumps(restaurantObject)
    