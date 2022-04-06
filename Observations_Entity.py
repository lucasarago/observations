from asyncio.windows_events import NULL
from turtle import st
import mysql.connector, os

content = ''

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'data15.txt')

with open(filename) as f:
    content = f.read()

max_characters = 4999
iterations = int((len(content) / max_characters))

mydb = mysql.connector.connect(
  host="localhost",
  user=os.environ.get('MYSQL_USER'),
  password=os.environ.get('MYSQL_PASSWORD'),
  database="observations"
)

mycursor = mydb.cursor()

''' 

#Create database
mycursor.execute("CREATE DATABASE observations")

#Confirm database exists
mycursor.execute("SHOW DATABASES")

#Confirm table exists
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#Create tables
mycursor.execute("CREATE TABLE observations (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT(3), weight FLOAT(10,2))")

mycursor.execute("CREATE TABLE event_listener_doc_proccess (id INT AUTO_INCREMENT PRIMARY KEY, INT eventId NOT NULL, observations VARCHAR(255))")
mycursor.execute("CREATE TABLE observations_entity (id INT AUTO_INCREMENT PRIMARY KEY, eventId INT NOT NULL, observations VARCHAR(4999))")

#Insert one row
observation = NULL

sql = "INSERT INTO event_listener_doc_proccess (eventId, observations) VALUES (%s, %s)"
val = (1, observation)
mycursor.execute(sql, val)

sql = "INSERT INTO observations_entity (eventId, observations) VALUES (%s, %s)"
val = (1, 'Hola')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

'''
if len(content) > max_characters:
  ini = 0
  end = max_characters
  observationEmpty = NULL
  canAddEvent = True

  for i in range(iterations):

    if(canAddEvent):
      sql = "INSERT INTO event_listener_doc_proccess (eventId, observations) VALUES (%s, %s)"
      val = (1, observationEmpty)
      mycursor.execute(sql, val)
      canAddEvent = False
    observation = content[ini:end]
    sql = "INSERT INTO observations_entity (eventId, observations, portion_index) VALUES (%s, %s, %s)"
    val = (1, observation, (str(ini) + '-' + str(end)))
    mycursor.execute(sql, val)

    if((end + max_characters) < len(content)):
      ini = end + 1
      end = end + max_characters
    else:
      ini = end + 1
      end = len(content)

    print(mycursor.rowcount, "record inserted.")

  mydb.commit()