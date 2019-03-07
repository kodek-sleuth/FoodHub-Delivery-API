import unittest
import pytest
from app import db, create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app=create_app(config_name='development')

migrate=Migrate(app, db)
manager=Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    tests=unittest.TestLoader().discover('./Tests', pattern='test*.py')
    report=unittest.TextTestRunner(verbosity=2).run(tests)

    if report.wasSuccessful():
        return 1
    
    else:
        return 0

if __name__=="__main__":
    manager.run()