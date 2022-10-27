import sqlite3 as sq
import os
from rich.console import Console as console
import getpass

class secure_request:

    def __init__(self) -> None:
        secure_request.__init__(self)        
    def secure_load(name,password):
            try:
                connection = sq.connect("data/data.db")
                curseur = connection.cursor()
                
                request1 = f"""select user_name from information where user_name = "{name}" """
                request = f"""select passwords from information where passwords = "{password}" """

                result = curseur.execute(request1)
                for i in result :
                    names = list(i)
                    for i in names : names = i
                while names!=name : name = input("user name > ")

                result2 = curseur.execute(request)
                for j in result2:
                    code = list(j)
                    for i in code : code = i
                while code!= password: getpass.getpass("password > ")
                    
            except Exception as e : print(e)

            connection.close()
    
    def __integrity__(self):
        pass
