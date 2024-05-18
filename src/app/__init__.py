from flask import Flask, request
from app.routes.home import home

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return request.url + " does not exist or has not yet been implemented"

app.register_blueprint(home, url_prefix="/home")
