import mysql.connector
from os import getenv
from dotenv import load_dotenv

load_dotenv()
username = getenv("USERNAME")
userpass = getenv("PASS")

class Product:

    def __init__(self, name, price, quantity, id_cat):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id_cat = id_cat


    def display_allproducts(self):

        try :

            connection = mysql.connector.connect(
                host = "localhost",
                user = username,
                password = userpass,
                database = "store"
            )
            usercurs = connection.cursor()

            usercurs.execute(
                """
                    SELECT name_prod, name_cat, price AS prix, quantity as quantite
                    FROM product JOIN category 
                    ON product.id_cat = category.id_cat;
                """
            )
            rows = usercurs.fetchall()
            for r in rows:
                print(r)
            usercurs.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Something went wrong: {error}")

