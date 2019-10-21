from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']='473a86cdd5ace3908fb6bdde8df66339'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db =SQLAlchemy(app)


from app import routes