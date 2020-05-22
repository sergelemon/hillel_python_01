from flask import Flask
from config import Config
from app.db import DB

app = Flask(__name__)
app.config.from_object(Config)
app.db = DB()

from app import routes
