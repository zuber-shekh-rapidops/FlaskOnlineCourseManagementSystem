import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# *********************************************CONFIGURATIONS**********************************************************
app=Flask(__name__)
BASEDIR=os.path.abspath(os.path.dirname(__name__))
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASEDIR,'online_course_management.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
Migrate(app,db)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

# *********************************************BLUEPRINTS**********************************************************
from online_course_app.main.views import main
from online_course_app.student.views import student

app.register_blueprint(main)
app.register_blueprint(student)

# *********************************************VIEWS**********************************************************
from online_course_app.main import views
from online_course_app.student import views