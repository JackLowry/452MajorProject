#render_template allows for other files to be called in return statements
from flask import Flask, render_template, request, url_for, redirect#import flask into this file and render_template
import random

import PIL
import json
from datetime import datetime
import mysql.connector #import SQL
from math import ceil

def optimize_delivery(curr_r, curr_c):

    with open("api_key.txt") as f:
        api_key = f.read()
    gmaps = googlemaps.Client(key=api_key)

    deliverers = [(40.50488500478356, -74.4670101053852),
    (40.523748244622425, -74.47182690442412),
    (40.501203991220244, -74.41227952116414)]

    min_time = float("inf")
    best_d = -1
    to_c = gmaps.directions(curr_r, curr_c, mode="driving")
    total_time = to_c[0]["legs"][0]["duration"]["value"]
    for i, d in enumerate(deliverers):
        to_r = gmaps.directions(d, curr_r, mode="driving")
        d_time = to_r[0]["legs"][0]["duration"]["value"]
        print(d_time)
        if d_time < min_time:
            min_time = d_time
            deliverers = i
    print(total_time, min_time)
    total_time = total_time + min_time
    return total_time


mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database ="RUDownBad_Database") #connect to database, bad practive since problems with multiple connecctions and errors can occur, but fine for single user only
mycursor = mydb.cursor()


restaurants = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"]

currentRestaurant = None #will update one a Restaurant is selected
currentUser = None #will update when  a user logs in

app = Flask(__name__)

print(__name__) 

@app.route('/', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def login(): #return some object to be displayed to the user | general python syntax for defining a function
    return render_template('home.html') #name='Irfan'



@app.route('/login_page', methods=['GET', 'POST'])
def login_page(): #name of function and name of route do not have to match
    if request.method == 'POST':
        name = request.form.get('UserName')
        password = request.form.get('Password')
        mycursor.execute("SELECT username, user_password, User_ID FROM User_Profile WHERE username = %s and user_password = %s;", (name,password))
        result = mycursor.fetchone()
        global currentUser
        if (result == None):
            return redirect(url_for('login_page'))
        if(name == result[0] and password == result[1]):
            currentUser = result[2]
            return redirect(url_for('select'))
        else:
            return redirect(url_for('login_page'))    
    return render_template('login.html')

@app.route('/services')
def services_page(): #name of function and name of route do not have to match
    return render_template('services.html')

@app.route('/contact')
def contact_page(): #name of function and name of route do not have to match
    return render_template('contact.html')

@app.route('/about_Us')
def about_Us(): #name of function and name of route do not have to match
    return render_template('about_Us.html')

@app.route('/select')
def select(): #name of function and name of route do not have to match
    return render_template('select.html')

@app.route('/filter', methods=['GET', 'POST'])
def filter(): #name of function and name of route do not have to match
    if request.method == 'POST':
        age = request.form.get('age')
        print(age)
        if age == '':
            age = 'age'
        print(age)
        campus = request.form.get('Campus')
        print(campus)
        gender = request.form.get('gender')
        print(gender)
        year = request.form.get('year')
        print(year)
        if year == 'Any':
            year = 'year'
        sex = request.form.get('sexual_orientation')
        print(sex)
        school = request.form.get('school')
        print(school)
        sql_select_query = 'SELECT username, campus, residence, age, gender year, sexual_orientation, major, bio, school FROM user_profile WHERE age = ' + str(age) + ' and campus = "' + str(campus) + '" and gender = "' + str(gender) + '" and year = "' + str(year) + '" and sexual_orientation = "' + str(sex) + '" and school = "' + str(school) + '" ORDER BY RAND() LIMIT1;'
        print(sql_select_query)
        mycursor.execute(sql_select_query)
        result = mycursor.fetchall()
        print(result)
    return render_template('filter.html')

@app.route('/chat')
def chat(): #name of function and name of route do not have to match
    return render_template('chat.html')


@app.route('/register', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        name = request.form.get('username')
        print(name)
        password = request.form.get('password')
        print(password)
        age = request.form.get('age')
        print(age)
        campus = request.form.get('Campus')
        print(campus)
        residence = request.form.get('Residence_Hall')
        print(residence)
        gender = request.form.get('gender')
        print(gender)
        year = request.form.get('year')
        print(year)
        orientation = request.form.get('sexual_orientation')
        print(orientation)
        major = request.form.get('major')
        print(major)
        school = request.form.get('school')
        print(school)
        bio = request.form.get('bio')
        print(bio)
        userID = random.randint(0, 1000000)
        print(userID)
        img = request.form.get('profile_picture')
        print(img)
        imagefile = request.files.get('profile_picture', '')
        mycursor.execute("INSERT INTO User_Profile(User_ID,username,user_password,campus,residence,age,gender,year,sexual_orientation, major, bio, school, profile_picture ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (userID, name, password, campus, residence, age, gender, year, orientation,major, bio, school, imagefile))
        mydb.commit()
        return redirect(url_for('login_page'))
    return render_template('registration_form.html')



if __name__ == "__main__":
    app.run()

