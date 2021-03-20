from flask import Flask, render_template
import os
app = Flask(__name__, template_folder= 'views')

#importar los controllers
from src.controllers import *

def start_app():
    app.run(debug=True, port=5000)