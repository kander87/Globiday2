from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt     
from flask_app import app, DATABASE
from flask import flash, session
from flask_app.models import model_user
from flask_app.models import model_holiday
from flask_app.models import model_country

import json, requests


class Calendar:
    def __init__(self, data):
        self.id = data['id']
        self.cal_name = data['cal_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']        
        self.user_id = data['user_id']
        self.holidays=[]

## shout out to Kurticus for helping me this this crazy town complicated method
    @classmethod
    def save_calendar_of_holidays_by_country_by_code(cls, countryCodes, data):
        results= []
        for countryCode in countryCodes:
            print(countryCode)
            api_req=requests.get("https://date.nager.at/api/v3/NextPublicHolidays/"+countryCode)
            next_results=json.loads(api_req.content)
            results= results+next_results
        query= "INSERT INTO calendars (cal_name, user_id) VALUES ( %(cal_name)s, %(id)s);"
        calendar_id=connectToMySQL(DATABASE).query_db(query, data)
        holiday_list= []
        for result in results:
            holiday_data={
                ** result,
                "id" : model_holiday.Holiday.is_holiday_already_in_db_add_if_not(result),
                "calendar_id": calendar_id
            }
            holiday_list.append(holiday_data)
        for holiday_data in holiday_list:
            print(holiday_data)
            query="INSERT INTO holidays_has_calendars (holiday_id, calendar_id) VALUES ( %(id)s, %(calendar_id)s)"
            connectToMySQL(DATABASE).query_db(query, holiday_data)
        return "something"

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM calendars JOIN users ON calendars.user_id =users.id JOIN holidays_has_calendars ON calendars.id =holidays_has_calendars.calendar_id JOIN holidays ON holidays.id = holidays_has_calendars.holiday_id WHERE calendars.id = %(id)s ORDER BY date;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        holiday_list=[]
        if results:
            this_calendar = cls(results[0])
            for row in results: 
                holiday_data={
                    **row,
                    'id':row['holidays.id'],
                }
                these_holidays =model_holiday.Holiday(holiday_data)
                holiday_list.append(these_holidays)
            this_calendar.holidays=holiday_list
            return this_calendar
        return False

    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM calendars WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM calendars JOIN users ON calendars.user_id = users.id WHERE users.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        all_calendars=[] 
        if results:
            for row in results:
                this_calendar=cls(row) 
                user_data={ 
                    'id': row['users.id'], 
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                    **row 
                }
                this_user = model_user.User(user_data)  
                this_calendar.maker=this_user 
                all_calendars.append(this_calendar)
        return all_calendars 
