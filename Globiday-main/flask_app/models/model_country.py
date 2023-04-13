from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt     
from flask_app import app, DATABASE
from flask import flash, session
from flask_app.models import model_calendar
from flask_app.models import model_holiday
from flask_app.models import model_country
import json, requests


class Country:
    def __init__(self, data):
        self.code = data['code']
        self.name= data['name']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM countries;"
        results = connectToMySQL(DATABASE).query_db(query)
        countries = []
        for country in results:
            countries.append(cls(country))
        return countries

    @classmethod
    def get_holidays_by_country_by_code(cls, countryCodes):
        results= []

        for countryCode in countryCodes:
            print(countryCode)
            api_req=requests.get("https://date.nager.at/api/v3/NextPublicHolidays/"+countryCode)
            data=json.loads(api_req.content)
            results= results+data
            
        return results
