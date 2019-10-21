import os
import datetime
import secrets
import pyowm
import googlemaps
import requests
from flask import render_template, url_for, flash, redirect, request, session
from app import app, db
from app.models import Task
from sqlalchemy.orm import sessionmaker
from app.cal_setup import get_calendar_service
from app.forms import DeleteEventForm
api_key ='AIzaSyC-A4N-t_5puJIGl9oaLN-g9Mm0MIlurfE'


@app.route("/")
def home():
    return render_template('home.html',title='home')

@app.route("/auth")
def auth():
	Task.query.delete()
	service = get_calendar_service()
	# Call the Calendar API
	now = datetime.datetime.utcnow().isoformat() + 'Z'
	print('Getting List o 10 events')
	events_result = service.events().list(
		calendarId='primary', timeMin=now,
		maxResults=10, singleEvents=True,
		orderBy='startTime').execute()
	events = events_result.get('items', [])
	
	if not events:
		print('No upcoming events found.')
	for event in events:
	
		start = event['start'].get('dateTime')
		end = event['end'].get('dateTime')
		start = start[:-9]
		end = end[:-9]
		start = datetime.datetime.strptime(start,"%Y-%m-%dT%H:%M")
		end = datetime.datetime.strptime(end,"%Y-%m-%dT%H:%M")
		start_time = start.strftime("%I:%M")
		start_date = start.strftime("%B %d, %Y")
		end_time = end.strftime("%I:%M")
		end_date = end.strftime("%B %d, %Y")
		location = event.get('location')
		summary = event['summary']
		eid = event['id']
		gm = googlemaps.Client(key=api_key)
		geocode_result = gm.geocode(location)[0]
		lat = geocode_result['geometry']['location']['lat']
		lng = geocode_result['geometry']['location']['lng']
		owm = pyowm.OWM('f105307850d1950df6f4f5728985c2d6')
		observation = owm.weather_at_coords(lat, lng)
		weather = observation.get_weather()
		dw = weather.get_detailed_status()  
		temp = weather.get_temperature('celsius')['temp']
		max = weather.get_temperature('celsius')['temp_max']
		min = weather.get_temperature('celsius')['temp_min']
		task = Task(eid=eid, start=start, end=end, location=location, summary=summary, weather=dw, temp=temp, max=max, min=min)
		db.session.add(task)
		db.session.commit()
	return read()
	   
@app.route("/read")
def read():
	return render_template('display.html', title='display', events = Task.query.all())