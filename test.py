from sklearn import tree
import mysql.connector

in_price = in_price.replace(",",".")
in_price = in_price.replace("$","")
in_mileage = in_mileage.replace(",",".")
x = []
y = []

def read_data():
    connector = mysql.connector.connect ( user = "root", password = '' , host = '127.0.0.1' , database = '')
    cursor = connector.cursor()
    syntax = (f"SELECT * FROM cars;")
    cursor.execute(syntax)
    for name,price,mileage in cursor:
        mileage = mileage.replace(",",".")
        price = price.replace("$","")
        price = price.replace(",",".")
        n_mileage = float(mileage)
        n_price = float(price)


read_data()

