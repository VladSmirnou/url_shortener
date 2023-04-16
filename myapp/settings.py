from environs import Env


env = Env()
env.read_env()

DEBUG = env.bool('FLASK_DEBUG', default=False)
FLASK_APP=env.str('FLASK_APP')
SECRET_KEY = env.str('SECRET_KEY')
SQLALCHEMY_DATABASE_URI=env.str('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS=env.bool('SQLALCHEMY_TRACK_MODIFICATIONS', default=False)

