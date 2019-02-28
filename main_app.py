from app import create_app
from app.Models import *

app=create_app(config_name='production')

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(port=3000)