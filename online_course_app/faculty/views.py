from flask import Blueprint,render_template,redirect,flash,url_for
from online_course_app.app import db
from online_course_app.faculty.forms import SignupForm,LoginForm
from online_course_app.student.forms import LoginForm
from online_course_app.faculty.models import FacultyModel
from flask_login import login_required,login_user,logout_user

faculty=Blueprint('faculty',__name__,url_prefix='/faculty')

@faculty.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        faculty=FacultyModel.query.filter_by(email=form.email.data).first()
        if faculty and faculty.check_password(form.password.data):
            login_user(faculty)
            flash('logged in successfully!')
            return redirect(url_for('faculty.home'))
        else:
            flash('invalid email or password')
            return redirect(url_for('faculty.login'))
    return render_template('faculty/login.html',form=form)

@faculty.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        faculty=FacultyModel(email=form.email.data,
            password=form.password.data,
            mobile=form.mobile.data,
            first_name=form.fname.data,
            last_name=form.lname.data,
            dob=form.dob.data,
            gender=form.gender.data)
        db.session.add(faculty)
        db.session.commit()
        flash('account created successfully!')
        return redirect(url_for('faculty.login'))
    return render_template('faculty/signup.html',form=form)


@faculty.route('/home')
@login_required
def home():
    return render_template('faculty/home.html')

@faculty.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout successfully!')
    return redirect(url_for('faculty.login'))