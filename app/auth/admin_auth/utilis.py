from app import *
from functools import wraps
from flask import current_app

def admin_Required(A):
    @wraps(A)
    def wrapper(*args, **kwargs):
        token=request.args.get('token')
        
        try:
            jwt.decode(token, current_app.config['ADMIN_SECRET_KEY'])
            return A(*args, **kwargs)
        
        except:
            return jsonify({"AUTH ERROR": "ADMIN AUTHORISATION REQUIRED"})
    
    return wrapper