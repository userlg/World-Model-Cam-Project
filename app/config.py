from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    CSRF_ENABLED = True
    TESTING = False
    #SERVER_NAME='WorldModelCam.com'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
    'host':'mongodb://localhost/wmc_db'
}

class ProductionConfig(Config):
   ENV = os.environ.get("prod_env")
   DEBUG = os.environ.get("prod_debug")
   MONGO_URI = os.environ.get("prod_mongo_uri")


class DevelopmentConfig(Config):
    ENV = os.environ.get("dev_env")
    DEBUG = os.environ.get("dev_debug")
    MONGO_URI = os.environ.get("dev_mongo_uri")

class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True