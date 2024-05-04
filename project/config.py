import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY=os.getenv('SECRET_KEY')
    USER_PSWD=os.getenv('USER_PSWD')
    ACCESS_KEY_ID=os.getenv('ACCESS_KEY_ID')
    SECRET_ACCESS_KEY=os.getenv('SECRET_ACCESS_KEY')
    AWS_REGION=os.getenv('AWS_REGION')
    BUCKET_NAME=os.getenv('BUCKET_NAME')
