import mysql.connector
from os import getenv
from dotenv import load_dotenv

load_dotenv()
username = getenv("USERNAME")
userpass = getenv("PASS")

class Category:

    def __init__(self, name):
        self.name = name

    def display_allcats(self):

        try :

            connection = mysql.connector.connect(
                host = "localhost",
                user = username,
                password = userpass,
                database = "store"
            )
            usercurs = connection.cursor()

            usercurs.execute(
                "SELECT * FROM category;"
            )
            rows = usercurs.fetchall()
            for r in rows:
                print(r)
            usercurs.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Something went wrong: {error}")


