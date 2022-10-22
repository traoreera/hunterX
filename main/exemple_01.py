
import os

from flask import Flask, make_response, render_template, request

# application Flask
script_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=f"{script_dir}/../templates", static_folder=f"{script_dir}/../static")



# class htm home definition 

class home :
    
    def __init__(self) -> None:

        # initialisation de valeur 
        
        home.__init__(self)
        self.home_title = "Alice deco"
        self.home_page = {}


    @app.route('/', methods = ["GET","POST"]) # page d'aceuiller
    def loads_login_page():

        if request.method == "":

            name = request.form.get('name')
            passewords = request.form.get('passewords')

            print(name, " : ", passewords)

        return make_response(render_template('index.html'))


    
    @app.route("/home", methods = ["GET","POST"])

    def homepage():
        return make_response(render_template('home.html'))
        


if __name__ == "__main__":

    app.config.update(ENV="development", DEBUG=True)

    app.run()