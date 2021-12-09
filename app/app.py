from flask import Flask, render_template, request, redirect, url_for
import os, requests, datetime


app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

@app.route('/')
def index():

    response = requests.get("https://api.nasa.gov/planetary/apod?api_key={}".format(API_KEY))
    r = response.json()
    return render_template('index.html', landing_image=r['hdurl'])
    

@app.route('/mars', methods=["GET", "POST"])
def mars():

    todaysDate = datetime.datetime.now().strftime('%Y-%m-%d')
    filter = request.form.get('filter', todaysDate)

    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={}&camera=fhaz&api_key={}".format(filter, API_KEY))
    r = response.json()
    return render_template('mars.html', photos=r['photos'], todaysDate=todaysDate)