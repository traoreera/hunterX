

import os

from flask import Flask, make_response, render_template, request

# application Flask
script_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=f"{script_dir}/../templates", static_folder=f"{script_dir}/../static")


class Main :
    
    def __init__(self):
        
        Main.__init__(self)\
            
    
    def srv_test():
        import requests
        url = "http://127.0.0.1:5000"
        payload={}
        headers = {}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        if reponse.ok:
            print ("ok")
        
        
    app.route("/")
    def home_page():
        return make_response(render_template('index.html'))
    
    
if __name__ == "__main__":
    
    app.config.update(ENV="development", DEBUG=True)
    Main.srv_test()
    app()
        