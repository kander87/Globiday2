from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt     
from flask_app import app, DATABASE
from flask import flash, session
from flask_app.models import model_calendar
from flask_app.models import model_holiday
from flask_app.models import model_country


class Holiday:
    def __init__(self, data):
        self.id = data['id']        
        self.date = data['date']
        self.local_name = data['local_name']
        self.name = data['name']
        self.fixed = data['fixed']
        self.launch_year = data['launch_year']
        self.country_code = data['country_code']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM holidays;"
        results = connectToMySQL(DATABASE).query_db(query)
        holidays = []
        for holiday in results:
            holidays.append(cls(holiday))
        return holidays

    @classmethod
    def create(cls, data):
        query = "INSERT INTO holidays ( date, local_name, name, fixed, launch_year , country_code) VALUES ( %(date)s , %(localName)s , %(name)s ,%(fixed)s, %(launchYear)s, %(countryCode)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def is_holiday_already_in_db_add_if_not(cls,data):
        query= "SELECT id FROM holidays WHERE local_name =%(localName)s AND country_code=%(countryCode)s AND date=%(date)s"
        result =connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return cls.create(data)
        return result[0]["id"]

    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM holidays WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )
