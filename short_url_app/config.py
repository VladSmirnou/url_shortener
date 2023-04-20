from environs import Env
from hashids import Hashids


env = Env()
env.read_env()

class Config:
    FLASK_DEBUG = env.bool('FLASK_DEBUG', default=False)
    SECRET_KEY = env.str('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=env.str('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=env.bool('SQLALCHEMY_TRACK_MODIFICATIONS', default=False)
    HASHIDS = Hashids(min_length=4, salt=env.str('SECRET_KEY'))