import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="minhanh0711",
  database="MyDB"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM MyDB")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
