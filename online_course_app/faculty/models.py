# **********************************************student/models.py**************************************************
from online_course_app.app import db,login_manager,bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return FacultyModel.query.get(int(id))

class FacultyModel(db.Model,UserMixin):
    __tablename__='faculty'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=False)
    password=db.Column(db.String(256),nullable=False)
    mobile=db.Column(db.Integer,nullable=False,)
    first_name=db.Column(db.String(30),nullable=False)
    last_name=db.Column(db.String(30),nullable=False)
    dob=db.Column(db.DateTime,nullable=False)
    gender=db.Column(db.String(20),nullable=False)
    profile_pic=db.Column(db.String(100),nullable=False,default='profile_pic.jpg')
    is_faculty=db.Column(db.Boolean,nullable=True,server_default="True")
    
    def __init__(self,email,password,mobile,first_name,last_name,dob,gender):
        self.username=str(email).split('@')[0]
        self.email=email
        self.password=bcrypt.generate_password_hash(password)
        self.mobile=mobile
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.gender=gender

    def __repr__(self):
        return f"hello i am {self.username}"


    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)