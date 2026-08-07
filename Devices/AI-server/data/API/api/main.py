from flask import Flask
from flask_cors import CORS
from config import()
from paths import()
from routes.ask import ask_bp
from routes.openapi import openapi_bp

app = Flask(__name__)
CORS(app)
