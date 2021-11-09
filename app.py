#render_template allows for other files to be called in return statements
from flask import Flask, render_template, request, url_for, redirect#import flask into this file and render_template
import random
import googlemaps
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


mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database ="FreshFood_Database") #connect to database, bad practive since problems with multiple connecctions and errors can occur, but fine for single user only
mycursor = mydb.cursor()


restaurants = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"]

currentRestaurant = None #will update one a Restaurant is selected
currentUser = None #will update when  a user logs in

app = Flask(__name__)

print(__name__) 

@app.route('/', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def login(): #return some object to be displayed to the user | general python syntax for defining a function
    if request.method == 'POST':
        name = request.form.get('UserName')
        password = request.form.get('Password')
        mycursor.execute("SELECT username, user_password, User_ID FROM User_Profile WHERE username = %s and user_password = %s;", (name,password))
        result = mycursor.fetchone()
        global currentUser
        if (result == None):
            return redirect(url_for('login'))
        if(name == result[0] and password == result[1]):
            currentUser = result[2]
            return redirect(url_for('dropdown'))
        else:
            return redirect(url_for('login'))
    return render_template('home.html') #name='Irfan'

@app.route('/about')
def about(): #name of function and name of route do not have to match
    return 'This is a url shortener'

@app.route('/register', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        zipcode = request.form.get('zipcode')
        phonenum = request.form.get('phoneNum')
        emailaddress = request.form.get('emailAddress')
        creditcard = request.form.get('creditCard')
        userID = random.randint(0, 1000000)
        mycursor.execute("INSERT INTO User_Profile(User_ID,city,state,street,country,zip_code,user_password,username,phoneNum,email_address,credit_card_number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
         (userID, city, state, street, country, zipcode, password, name, phonenum,emailaddress,creditcard))
        mydb.commit()
        return redirect(url_for('login'))
    return render_template('registration_form.html')

@app.route('/Restaurant', methods=['GET', 'POST'])
def dropdown():
    if request.method == 'POST':
        rest = request.form.get("Restaurants")
        global currentRestaurant
        mycursor.execute("SELECT RestaurantID FROM Restaurant where RestaurantName = '"+ rest +"';")
        result = mycursor.fetchone()    
        currentRestaurant = result[0]
        print(currentRestaurant)
        return redirect(url_for('menu'))
    mycursor.execute("select  RestaurantName from Restaurant;")
    result = mycursor.fetchall()
    rows=[i[0] for i in result]
    return render_template('dropdown.html', content = rows)

@app.route('/menu', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def menu(): #return some object to be displayed to the user | general python syntax for defining a function
    if request.method == 'POST':

        return redirect(url_for('orderStats'))
    mycursor.execute("select  Dish_Name from foodMenu where RestaurantID = '"+ str(currentRestaurant) +"';")
    result = mycursor.fetchall()
    rows=[i[0] for i in result]
    mycursor.execute("select Dish_Name, Price from foodMenu where RestaurantID = '"+ str(currentRestaurant) +"';")
    result2 =mycursor.fetchall()
    rows2 =  result2
    return render_template('menu.html', content = rows, prices = rows2) #name='Irfan'

@app.route('/orderStats', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def orderStats(): #return some object to be displayed to the user | general python syntax for defining a function
    if request.method == 'POST':
        return redirect(url_for('login'))
    global currentUser, currentRestaurant
    mycursor.execute("select street, city, state, country, zip_code from Restaurant where RestaurantID = '"+ str(currentRestaurant) +"';")
    restaurant_loc = ' '.join(mycursor.fetchall()[0])
    mycursor.execute("select street, city, state, country, zip_code from User_Profile where User_ID = '"+ str(currentUser) +"';")
    user_loc = ' '.join(mycursor.fetchall()[0])
    time_to_deliver = ceil(optimize_delivery(restaurant_loc, user_loc)/60)
    print(restaurant_loc, user_loc, time_to_deliver)
    return render_template('orderStats.html', delivery_time=time_to_deliver) #name='Irfan'

if __name__ == "__main__":
    app.run()

