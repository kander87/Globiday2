# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "Your secret key here"

DATABASE = "your schema from mysql here"

