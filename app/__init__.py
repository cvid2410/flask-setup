from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

if app.config['ENV'] == "production":
    app.config.from_object('app.config.ProductionConfig')
elif app.config['ENV'] == "testing":
    app.config.from_object('app.config.TestingConfig')
else:
    app.config.from_object('app.config.DevelopmentConfig')

db = SQLAlchemy(app)

from .models import *
from .views import *

migrate = Migrate(app, db)


