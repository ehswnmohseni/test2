#this program insert some data to database!
import mysql.connector

#make connection to database
connector = mysql.connector.connect ( user = "root", password = 'its*not*password' , host = '127.0.0.1' , database = 'learn')

#make cursor
cursor = connector.cursor()

#write mysql function
cursor.execute("INSERT INTO person VALUES ('ha','m','26')")

#ready to finish?!
connector.commit()

#Done close it!
connector.close()

#make connection to database twice
connector = mysql.connector.connect ( user = "root", password = 'its*not*password' , host = '127.0.0.1' , database = 'learn')

#make cursor
cursor = connector.cursor()

#write mysql function in variable 
query = ("SELECT * FROM person;")
cursor.execute(query)

#make loop on database table's
for (name,sex,age) in cursor:
    if sex == "m":
        print(f"His name is {name} and He have {age} years old!")

    else:
        print(f"Her name is {name} and She have {age} years old!")
