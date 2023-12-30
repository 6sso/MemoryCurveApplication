from flask import Flask, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import render_template
import os

app = Flask(__name__)
#CORS(app)  # autorise toutes les origines pour simplifier

@app.route('/') #On définit une route avec entre guillemets le chemin de cette route.
# ici c'est notre page d'accueil donc on met juste un /
def home():
    #return "<h1>hello world</h1>"
    return render_template("accueil.html")

@app.route("/visualisation")
def visu():
    return render_template("visualisation.html")

if __name__ =='__main__': #si le fichier python sur lequel on est est exécuté en tant que programme et pas en tant que module :
    app.run(debug=True, host='127.0.0.1', port = 8000) #alors on run l'app
