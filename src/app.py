from flask import Flask
from .config import app_config



def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)


  app.config.from_object(app_config[env_name])


  db.init_app(app) 

  
  app.register_blueprint(contact_blueprint, url_prefix='/api/v1/contacts')


  return app