import os
class Config:
    pass
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://",1)
   
    pass
class TestConfig(Config):
    
    pass
class DevConfig(Config):    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://code_world:haimy@localhost/waimina'
    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}