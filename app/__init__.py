import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder=None)

app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

from app.views import rides
app.register_blueprint(rides, use_prefix='/rides')

db = SQLAlchemy(app)
