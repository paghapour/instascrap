import mysql.connector
import instaloader

from insta import instagram

mydb = mysql.connector.Connect(
    host = "localhost",
    user = "pooria",
    password = "",
    database = "mydatabase"
)
'''
user = instagram()

mycursor = mydb.cursor()
sql = "INSERT INTO customers(followers , followees) VALUES(%s , %s)"
val = (
    user.followers,
    user.followees
)
mycursor.execute(sql ,  val)
mydb.commit()
'''