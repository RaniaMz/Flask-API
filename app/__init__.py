from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mariadb@127.0.0.1/HRapp'
db = SQLAlchemy(app)
app.config['UPLOAD_EXTENSIONS'] = ['pdf', 'docs']
app.config['UPLOAD_PATH'] = 'uploads'
app.config["IS_CLOUD"] = False
from app.models import *

db.create_all()

from app import views
from app import admin_views
