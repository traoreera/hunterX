import sqlite3 as sql
import os
from rich.console import Console as console

class creating:

    def __init__(self) -> None:
        creating.__init__(self)

        self.data = "data.db"
        self.dir = "/data"
        self.pwd= "{%d,%d,%s} login filead ..."

    def verificatioN(self):
        # verification
        if os.path.exists("data.sqlite") : 


            console.log("database already exist ...") # verification de la base de donne
            connection = sql.connect('data.sql')
            curseur = connection.cursor()

            try : curseur.execute("select * from information")

            except Exception :
                console.log("imposible de se connecte a la base de donnes [?] ...")
                
        else :

            console.log()
            print("Vous avez suprimmer la base de donnes fichier innexsistant [!]")
        