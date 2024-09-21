import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://user:password@db/flask_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
