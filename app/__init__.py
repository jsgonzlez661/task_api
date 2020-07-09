from flask import Flask 
import config

app = Flask(__name__)
app.config.from_object(config.ProductionConfig)

from app.routes.routes import *