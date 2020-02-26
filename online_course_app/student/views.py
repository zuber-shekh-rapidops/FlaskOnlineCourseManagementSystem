from flask import Blueprint,render_template,redirect,url_for,flash
from online_course_app.app import db
from online_course_app.student.forms import LoginForm,SignupForm
from online_course_app.student.models import StudentModel
from flask_login import login_required,login_user,logout_user

student=Blueprint('student',__name__,url_prefix='/student')

# student/login
@student.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        student=StudentModel.query.filter_by(email=form.email.data).first()
        if student and student.check_password(form.password.data):
            login_user(student)
            flash('logged in successfully!')
            return redirect(url_for('student.home'))
        else:
            flash('invalid email or password')
            return redirect(url_for('student.login'))
    return render_template('student/login.html',form=form)

# student/signup
@student.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        student=StudentModel(email=form.email.data,
            password=form.password.data,
            mobile=form.mobile.data,
            first_name=form.fname.data,
            last_name=form.lname.data,
            dob=form.dob.data,
            gender=form.gender.data)
        db.session.add(student)
        db.session.commit()
        flash('account created successfully!')
        return redirect(url_for('student.login'))
    return render_template('student/signup.html',form=form)


# student/home
@student.route('/home')
@login_required
def home():
    return render_template('student/home.html')


# student/home
@student.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout successfully!')
    return redirect(url_for('student.login'))
