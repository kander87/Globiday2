from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt     
from flask_app import app, DATABASE
from flask import flash, session
from flask_app.models import model_calendar
from flask_app.models import model_holiday
from flask_app.models import model_country


class Holidays_has_calendars:
    def __init__(self, data):
        self.holiday_id = data['holiday_id']
        self.calendar_id = data['calendar_id']
