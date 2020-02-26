# faculty/models.py
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,RadioField,IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from online_course_app.faculty.models import FacultyModel



class LoginForm(FlaskForm):

    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('login')

class SignupForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    mobile=IntegerField('mobile',validators=[DataRequired()])
    fname=StringField('first name',validators=[DataRequired()])
    lname=StringField('last name',validators=[DataRequired()])
    dob=DateField('date of birth',validators=[DataRequired()])
    gender=RadioField('gender',validators=[DataRequired()],choices=[('male','male'),('female','female'),('other','other')])
    password=PasswordField('password',validators=[DataRequired()])
    cpassword=PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('signup')

    def validate_email(self,email):
        student=FacultyModel.query.filter_by(email=email.data).first()
        if student:
            raise ValidationError('email is already registred!')

    def validate_mobile(self,mobile):
        student=FacultyModel.query.filter_by(mobile=mobile.data).first()
        if student:
            raise ValidationError('mobile number is already registred!')
