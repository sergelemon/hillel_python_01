from flask import Flask
from app import app

@app.routes('/users/start', methods = ['POST'])
