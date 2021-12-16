import mysql.connector
import time
import random
import os
from PIL import Image

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "xxxx", database ="RUDownBad_Database2")

#Run this file to test database connection


# to fill it our, since we are poor we are all going to have localhost and root as our user. When you install sql
#your password should be the same as what you set it as so your connection line should look like

#mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Change This to Yours")

if (mydb == None):
    print = ("Connection failure")


else:
    print("connected")
    print(mydb)

mycursor = mydb.cursor()

# time inserting 100, 1000, 10000 samples into database
# change userid each time randomly large number
# find average time per insert

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

name = 'Test Name'
password = 'testpassword'
campus = 'Test Campus'
residence = 'Test Residence'
age = '23'
gender = 'Test Gender'
year = 'Test Year'
orientation = 'Test Orientation'
major = 'Test Major'
bio = 'Test Bio'
school = 'Test School'
profile_pic = convertToBinaryData('pepebusiness.png')

N = 100

start = time.time()
for x in range(N):
    userID = random.randint(0, 1000000000)   
    mycursor.execute("INSERT INTO User_Profile(User_ID,username,user_password,campus,residence,age,gender,year,sexual_orientation, major, bio, school, profile_picture) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
        (userID, name, password, campus, residence, age, gender, year, orientation,major, bio, school, profile_pic))
    mydb.commit()
end = time.time()
total_time = end - start
avg_time = total_time/N

print('Total time 100 Inserts: ' + str(total_time))
print('Avg time: 100 Inserts' + str(avg_time))

N = 1000

start = time.time()
for x in range(N):
    userID = random.randint(0, 1000000000)   
    mycursor.execute("INSERT INTO User_Profile(User_ID,username,user_password,campus,residence,age,gender,year,sexual_orientation, major, bio, school, profile_picture) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
        (userID, name, password, campus, residence, age, gender, year, orientation,major, bio, school, profile_pic))
    mydb.commit()
end = time.time()
total_time = end - start
avg_time = total_time/N

print('Total time 1000 Inserts: ' + str(total_time))
print('Avg time: 1000 Inserts' + str(avg_time))

N = 10000

start = time.time()
for x in range(N):
    userID = random.randint(0, 1000000000)   
    mycursor.execute("INSERT INTO User_Profile(User_ID,username,user_password,campus,residence,age,gender,year,sexual_orientation, major, bio, school, profile_picture) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
        (userID, name, password, campus, residence, age, gender, year, orientation,major, bio, school, profile_pic))
    mydb.commit()
end = time.time()
total_time = end - start
avg_time = total_time/N

print('Total time 10000 Inserts: ' + str(total_time))
print('Avg time: 10000 Inserts' + str(avg_time))

N = 100

start = time.time()
for x in range(N):
    mycursor.execute("SELECT User_ID, username, campus, residence, age, gender, year, sexual_orientation, major, bio, school from User_Profile ORDER BY RAND() LIMIT 1;")
    result = mycursor.fetchall() 
end = time.time()
total_time = end - start
avg_time = total_time/N

print('Total time 100 Fetches: ' + str(total_time))
print('Avg time: 100 Fetches' + str(avg_time))

N = 1000

start = time.time()
for x in range(N):
    mycursor.execute("SELECT User_ID, username, campus, residence, age, gender, year, sexual_orientation, major, bio, school from User_Profile ORDER BY RAND() LIMIT 1;")
    result = mycursor.fetchall() 
end = time.time()
total_time = end - start
avg_time = total_time/N

print('Total time 100 Fetches: ' + str(total_time))
print('Avg time: 100 Fetches' + str(avg_time))

N = 10000

start = time.time()
for x in range(N):
    mycursor.execute("SELECT User_ID, username, campus, residence, age, gender, year, sexual_orientation, major, bio, school from User_Profile ORDER BY RAND() LIMIT 1;")
    result = mycursor.fetchall() 
end = time.time()
total_time = end - start
avg_time = total_time/N

print('Total time 100 Fetches: ' + str(total_time))
print('Avg time: 100 Fetches' + str(avg_time))