from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.model_user import User 
from flask_app.models.model_calendar import Calendar 
from flask_app.models.model_country import Country 
from flask_app.controllers import controller_user 
from flask_app.controllers import controller_country


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def intro():
    if "user_id" in session:
        del session["user_id"]
    return render_template("intro.html") 

@app.route('/login')
def login():
    if "user_id" in session:
        del session["user_id"]
    return render_template("login.html") 

@app.route('/register')
def register():
    if "user_id" in session:
        del session["user_id"]
    return render_template("register.html") 


#Hashing Upon Registration
@app.route('/register/user', methods=['POST'])
def registerUser():
    if not User.validate_user(request.form):
        return redirect('/register')
    # if reque
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password']),
        "confirm_password": bcrypt.generate_password_hash(request.form['confirm_password'])
    }

    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/calendars')


#Comparing Upon Login
@app.route('/login', methods=['POST'])
def loginUser():
    print(request.form['email'])
    user_in_db = User.get_by_email(request.form)

    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/login')
    session['user_id'] = user_in_db.id
    return redirect("/calendars")


@app.route('/calendars')
def success():
    if "user_id" not in session:
        return redirect('/')
    if "country_codes" in session:
        del session['country_codes']
    data ={
        "id": session["user_id"]
    }
    user_in_db =User.get_by_id(data)
    all_calendars = Calendar.get_all({'id':session['user_id']})
    return render_template("dashboard_calendar.html", user_in_db =user_in_db, all_calendars=all_calendars) 