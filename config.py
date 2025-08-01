import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://smartuser:smartpass123@localhost:3306/smartcam'
    SQLALCHEMY_TRACK_MODIFICATIONS = False