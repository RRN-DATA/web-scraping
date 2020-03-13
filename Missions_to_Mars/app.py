# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template
import pymongo

#from scrape_mars import LoadScrapeClass
import pandas as pd

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.nasa_data
collection = db.mars_data

# List of Dictionaries of hemi_images


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    mars = list(db.collection.find())
    print(mars)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars=mars)


if __name__ == "__main__":
    app.run(debug=True)
