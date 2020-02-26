import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# *********************************************CONFIGURATIONS**********************************************************
app=Flask(__name__)
BASEDIR=os.path.abspath(os.path.dirname(__name__))
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASEDIR,'online_course_management.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
Migrate(app,db)

# *********************************************BLUEPRINTS**********************************************************
from online_course_app.main.views import main

app.register_blueprint(main)

# *********************************************VIEWS**********************************************************
from online_course_app.main import views