from sklearn import tree
import mysql.connector

print("hahahahaha")

in_price = input("enter the price\n($19,000):")
in_mileage = input("enter the price\n(101,813):")
in_price = in_price.replace(",",".")
in_price = in_price.replace("$","")
in_mileage = in_mileage.replace(",",".")
x = []
y = []



def read_data():
    connector = mysql.connector.connect ( user = "root", password = '313E.m313' , host = '127.0.0.1' , database = 'finall')
    cursor = connector.cursor()
    syntax = (f"SELECT * FROM car;")
    cursor.execute(syntax)
    for name,price,mileage in cursor:
        mileage = mileage.replace(",",".")
        price = price.replace("$","")
        price = price.replace(",",".")
        n_mileage = float(mileage)
        n_price = float(price)
        use_data(name,n_price,n_mileage)

def use_data(name,n_price,n_mileage):
    ready = [n_mileage,n_price]
    x.append(ready)
    y.append(name)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)
    answer = clf.predict([in_price,in_mileage])
    print(answer)

read_data()
