from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object(Config)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)