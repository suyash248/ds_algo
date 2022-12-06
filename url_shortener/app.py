from flask import Flask, request, redirect
from .service.shorener_service import ShortenerService

app = Flask(__name__)
shortener_service: ShortenerService = ShortenerService()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/shorten", methods=["POST"])
def shorten():
    print(request.json)
    # TODO - rqeuest param validation
    short_url = shortener_service.generate_short_url(request.json['raw_url'])
    return "localhost:5000/redirect/{}".format(short_url) # TODO -Need to get the base_url from config

@app.route("/redirect/<short_url>", methods=["GET"])
def redirect_to_raw_url(short_url):
    raw_url = shortener_service.get_raw_url(short_url)
    return "<p><a href='{}'>Redirect</a></p>".format(raw_url)
