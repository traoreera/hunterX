
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
    def previsualisation():
        
        import requests
        url = "http://127.0.0.1:5000"
        payload={}
        headers = {}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        print(response.text)
        return make_response(render_template('slide.html'))


    @app.route('/home')
    def home():

        return make_response(render_template('home.html'))

        
if __name__ == "__main__":

    app.config.update(ENV="development", DEBUG=True)

    app.run()
    
    
