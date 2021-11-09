import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "3072", database ="FreshFood_Database")


# to fill it our, since we are poor we are all going to have localhost and root as our user. When you install sql
#your password should be the same as what you set it as so your connection line should look like

#mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Change This to Yours")

if (mydb == None):
    print = ("Connection failure")


else:
    print("connected")
    print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select * from User_Profile")

for i in mycursor:
    print(i)