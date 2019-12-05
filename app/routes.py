from flask import request, render_template, redirect, url_for # Import to do all routing stuff
from app import app # Import app to use routes 


@app.route('/')
def index():
	return render_template('index.html')