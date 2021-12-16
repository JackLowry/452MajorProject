#render_template allows for other files to be called in return statements
from flask import Flask, render_template, request, url_for, redirect#import flask into this file and render_template
import random

import googlemaps
import PIL
import json
from datetime import datetime
import mysql.connector #import SQL
from math import ceil
import base64

def get_distance(person_1, person_2):

    with open("api_key.txt") as f:
        api_key = f.read()
    gmaps = googlemaps.Client(key=api_key)

    try:
        ret_val = gmaps.directions(person_1, person_2, mode="driving")
    except googlemaps.exceptions.ApiError:
        return None
    time = ret_val[0]["legs"][0]["duration"]["value"]
    
    return float(time)/60

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open("static/profile.png", 'wb') as file:
        file.write(data)


mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database ="RUDownBad_Database") #connect to database, bad practive since problems with multiple connecctions and errors can occur, but fine for single user only
mycursor = mydb.cursor()



currentRestaurant = None #will update one a Restaurant is selected
currentUser = None #will update when  a user logs in
globalCampus = None
globalYear = None
globalSex = None
globalSchool = None
globalGender = None
myLocation = None
theirLocation = None
globalCurrOtherUserID = None
globalCurrInfo = None

globalTravelTime = None

app = Flask(__name__)

print(__name__) 

@app.route('/', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def login(): #return some object to be displayed to the user | general python syntax for defining a function
    global currentUser
    currentUser = None
    return render_template('home.html') #name='Irfan'



@app.route('/login_page', methods=['GET', 'POST'])
def login_page(): #name of function and name of route do not have to match
    if request.method == 'POST':
        name = request.form.get('UserName')
        password = request.form.get('Password')
        mycursor.execute("SELECT username, user_password, User_ID, residence FROM User_Profile WHERE username = %s and user_password = %s;", (name,password))
        result = mycursor.fetchone()
        global currentUser
        global myLocation
        myLocation = result[3]
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
        campus = request.form.get('Campus')
        print(campus)
        gender = request.form.get('gender')
        print(gender)
        year = request.form.get('year')
        print(year)
        if year == 'Any':
            year = '*'
        sex = request.form.get('sexual_orientation')
        print(sex)
        school = request.form.get('school')
        print(school)
        sql_select_query = 'SELECT username, campus, residence, age, gender, year, sexual_orientation, major, bio, school, User_ID FROM User_Profile WHERE campus = "' + str(campus) + '" and gender = "' + str(gender) + '" and year = "' + str(year) + '" and sexual_orientation = "' + str(sex) + '" and school = "' + str(school) + '" ORDER BY RAND() LIMIT 1;'
        print(sql_select_query)
        mycursor.execute(sql_select_query)
        result = mycursor.fetchall()
        print(result)
        global globalCampus 
        globalCampus = campus
        global globalYear 
        globalYear = year
        global globalSex 
        globalSex = sex
        global globalSchool
        globalSchool = school
        global globalGender 
        globalGender = gender 
        global globalCurrInfo 
        globalCurrInfo = result
        OtherID = None
        OtherID = result[0][10]
        global theirLocation
        theirLocation = result[0][2]
        print(OtherID)
        global globalCurrOtherUserID
        globalCurrOtherUserID = OtherID
        #saving all this information for use in the next page
        return redirect(url_for('profile_page'))  
    return render_template('filter.html')


@app.route('/profiles',  methods=['GET', 'POST'])
def profile_page(): #name of function and name of route do not have to match
    global theirLocation
    if request.method == 'POST':
        action = request.form.get('action')
        if (action == 'mingle'):
            global globalCurrOtherUserID
            global currentUser
            mycursor.execute("INSERT INTO Likes(User_ID,User_ID2) VALUES (%s,%s)",
            (currentUser, globalCurrOtherUserID))
            mydb.commit()
        global globalCampus 
        global globalYear 
        global globalSex 
        global globalSchool
        global globalGender 
        global globalCurrInfo 
        global globalTravelTime
        campus = globalCampus
        gender = globalGender
        sex = globalSex
        school = globalSchool
        gender = globalGender
        year = globalYear
        sql_select_query = 'SELECT username, campus, residence, age, gender, year, sexual_orientation, major, bio, school, User_ID FROM user_profile WHERE campus = "' + str(campus) + '" and gender = "' + str(gender) + '" and year = "' + str(year) + '" and sexual_orientation = "' + str(sex) + '" and school = "' + str(school) + '" ORDER BY RAND() LIMIT 1;'
        mycursor.execute(sql_select_query)
        result = mycursor.fetchall()        
        global globalCurrInfo 
        globalCurrInfo = result
        OtherID = None
        OtherID = result[0][10]
        print(OtherID)
        theirLocation = result[0][2]

        globalCurrOtherUserID = OtherID
        return redirect(url_for('profile_page'))  
    profileInfo = globalCurrInfo
    global myLocation
    currID = globalCurrOtherUserID
    sql_select_query = 'SELECT profile_picture FROM user_profile WHERE User_ID = "' + str(currID) + '" ;'
    print(sql_select_query)
    mycursor.execute(sql_select_query)
    result = mycursor.fetchall()
    profile_picture = result[0][0]
    profile_picture = write_file(profile_picture, "photo")
    print(profileInfo)
    # print(profile_picture)
    return render_template('profiles.html', content = profileInfo, picture = profile_picture, time=get_distance(myLocation + " New Brunswick, NJ", theirLocation + " New Brunswick, NJ"))

@app.route('/chat')
def chat(): #name of function and name of route do not have to match
    global currentUser
    currID = currentUser
    sql_select_query = 'SELECT * from likes WHERE User_ID = "' + str(currID) + '" ;'
    print(sql_select_query)
    mycursor.execute(sql_select_query)
    matches = mycursor.fetchall()
    matches = [matches]
    return render_template('chat.html', content = matches)


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
        if 'profile_picture' not in request.files:
            print('no file recieved')
        # img = request.form.get('profile_picture')
        # print(img)
        # imagefile = request.files.get('profile_picture', '')
        # print(imagefile)
        imagefile2 = request.files['profile_picture'].read()
        mycursor.execute("INSERT INTO User_Profile(User_ID,username,user_password,campus,residence,age,gender,year,sexual_orientation, major, bio, school, profile_picture ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (userID, name, password, campus, residence, age, gender, year, orientation,major, bio, school, imagefile2))
        mydb.commit()
        return redirect(url_for('login_page'))
    return render_template('registration_form.html')



if __name__ == "__main__":
    app.run()