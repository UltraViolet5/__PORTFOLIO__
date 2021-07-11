import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
        user_name=os.environ.get('USER_NAME'),
        password=os.environ.get('PASSWORD'),
        host=os.environ.get('HOST'),
        database_name=os.environ.get('DB_NAME')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
