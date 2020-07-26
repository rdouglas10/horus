from flask import Flask
from .config import app_config
from .models import db, bcrypt
from flask_cors import CORS
from .controllers.ContactController import contact_api as contact_blueprint


def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)
  cors = CORS(app, resources={r"/api/v1/contacts*": {"origins": "*"}})
  cors = CORS(app, resources={r"/api/v1/contacts/edit/<int:contact_id>*": {"origins": "*"}})

  app.config.from_object(app_config[env_name])

  # initializing bcrypt
  # bcrypt.init_app(app) 

  db.init_app(app) 

  
  app.register_blueprint(contact_blueprint, url_prefix='/api/v1/contacts')


  return app