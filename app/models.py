from datetime import datetime
from app import db


class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	eid = db.Column(db.String(100), nullable=False)
	start = db.Column(db.DateTime(100), nullable=False)
	end = db.Column(db.DateTime(100), nullable=False)
	location = db.Column(db.String(100), nullable=False)
	summary = db.Column(db.String(100), nullable=False)
	weather = db.Column(db.String(100), nullable=False)
	temp = db.Column(db.String(100), nullable=False)
	min = db.Column(db.String(100), nullable=False)
	max = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return f"Task('{self.eid}','{self.start}','{self.end}','{self.location}','{self.summary}','{self.weather}','{self.temp}','{self.min}','{self.max}')"
		
