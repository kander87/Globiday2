from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.model_user import User 
from flask_app.models.model_calendar import Calendar 
from flask_app.controllers import controller_user 
from flask_app.controllers import controller_country

from flask_app.models.model_country import Country 

@app.route('/calendar/view/<int:id>')
def calendar_view(id):
    if "user_id" not in session:
        return redirect('/')
    data={
        'id': id
    }
    user_data={
        'id' : session['user_id']
    }
    print("showing calendar")
    return render_template("view_calendar.html",  user=User.get_by_id(user_data), this_calendar=Calendar.get_by_id(data))

@app.route('/calendar/delete/<int:id>')
def delete(id):
    data = { 
    'id' : id
    }    
    Calendar.delete(data)
    print("deleting calendar")
    return redirect("/calendars")


# @app.route('/calendar/edit/<int:id>')
# def calendar_edit(id):
#     if "user_id" not in session:
#         return redirect('/')
#     data={
#         'id': id
#     }
#     user_data={
#         'id' : session['user_id']
#     }
#     edit=Calendar.get_by_id(data)
#     user=User.get_by_id(user_data)
#     return render_template("calendar_edit.html", edit=edit, user=user) 

# @app.route('/calendar/update/<int:id>', methods=['POST'])
# def calendar_update(id):
#     if "user_id" not in session:
#         return redirect('/')
#     data = { 
#       get clendar data here
#     }   
#     if not Calendar.validate_calendar(request.form):
#         return redirect (f"/calendar/edit/{request.form['edit_id']}")
#     print(request.form['edit_id'])
#     # Calendar.validate_calendar(request.form)
#     Calendar.edit(data)
#     print("editing calendar")
#     return redirect('/calendars')

