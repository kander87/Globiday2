from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.model_user import User 
from flask_app.models.model_calendar import Calendar 
from flask_app.models.model_country import Country 
from flask_app.controllers import controller_user 
from flask_app.controllers import controller_country


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/add/countries')
def add_countries():
    if "user_id" not in session:
        return redirect('/')
    data={
        'id': session['user_id']
    }
    return render_template("add_countries.html", user=User.get_by_id(data)) 


@app.route('/create/calendar', methods=["POST"])
def country_add():
    if "user_id" not in session:
        return redirect('/')

    countryCodes= request.form.getlist('countryCheckbox')
    session['country_codes']=countryCodes
    Country.get_holidays_by_country_by_code(countryCodes)
    print(session['country_codes'])
    print("adding countries")
    return redirect('/check/calendar')

@app.route('/check/calendar')
def check_calendar():
    if "user_id" not in session:
        return redirect('/')
    data={
        'id': session['user_id']
    }
    user_countries= session['country_codes']
    return render_template("check_calendar.html", user=User.get_by_id(data), user_countries=user_countries)

@app.route('/save/calendar')
def save_calendar():
    if "user_id" not in session:
        return redirect('/')
    data={
        'id': session['user_id']
    }
    user_countries= session['country_codes']
    user_countries_holidays=Country.get_holidays_by_country_by_code(user_countries)

    return render_template("save_calendar.html", user=User.get_by_id(data), user_countries=user_countries, user_countries_holidays=user_countries_holidays)

@app.route('/calendar/saved', methods=["POST"])
def saved_calendar():
    if "user_id" not in session:
        return redirect('/')
    data={
        'id': session['user_id'],
        'cal_name':request.form['cal_name'],
    }
    countryCodes= session['country_codes']
    Calendar.save_calendar_of_holidays_by_country_by_code(countryCodes,data)
    print('cal_name')
    print("Saving Calendar")
    return redirect ("/calendars") 
