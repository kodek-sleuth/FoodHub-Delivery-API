import sqlite3
import os
class Config():
    USER_SECRET_KEY='its nolonger a secret'
    ADMIN_SECRET_KEY='secret'
    SQLALCHEMY_TRACK_MODIFICATIONS=False 
    SQLALCHEMY_DATABASE_URI='postgresql://josekodek:kevina52@localhost:5432/foodhub'

class DevelopmentConfig(Config):
    DEBUG=True
    DEVELOPMENT=True
    USER_SECRET_KEY='its nolonger a secret'
    ADMIN_SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False 
    
class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    DEBUG=True
    TESTING=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    USER_SECRET_KEY='i wont tell if you dont'
    ADMIN_SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:believe@localhost:5432/fortestsonly'


class StagingConfig(Config):
    DEBUG=True
    DEVELOPMENT=True
    USER_SECRET_KEY='its nolonger a secret'
    ADMIN_SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI='postgresql://josekodek:kevina52@localhost:5432/foodhub'
    SQLALCHEMY_TRACK_MODIFICATIONS=False 

class ProductionConfig(Config):
    DEBUG=False
    TESTING=False
    USER_SECRET_KEY='its nolonger a secret'
    ADMIN_SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI= 'postgres://mutuzlpuljivzw:69a338c640a2fc6274a6e7992b7ce15efb72c6530aee22bca98e5a47a9d4f5f2@ec2-50-17-193-83.compute-1.amazonaws.com:5432/d32n5c5v10hgof'
    SQLALCHEMY_TRACK_MODIFICATIONS=False 


app_config={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}