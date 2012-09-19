# -*- coding: utf-8 -*-
import os

# Retrieve Flask, our framework
from flask import Flask

# create the Flask app
app = Flask(__name__)

# Main Page Route
@app.route("/")
def index():
    return "Hello World!<br/><br/><a href='/page2'>Visit page #2</a>"


# Second Page Route
@app.route("/page2")
def page2():
	return """<html><body>
	<h2>Welcome to page 2</h2>
	<p>This is just amazing!</p>
	</body></html>"""


# start the webserver
if __name__ == "__main__":
	app.debug = True
	app.run()