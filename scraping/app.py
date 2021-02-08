<<<<<<< HEAD
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route('/')
def home():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scraper():
    mars_dict = mongo.db.mars
    mars_dict_data = scrape_mars.scrape()
    mars_dict.update({}, mars_dict_data, upsert=True)
    return redirect('/', code = 302)

if __name__ == "__main__":
=======
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route('/')
def home():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scraper():
    mars_dict = mongo.db.mars
    mars_dict_data = scrape_mars.scrape()
    mars_dict.update({}, mars_dict_data, upsert=True)
    return redirect('/', code = 302)

if __name__ == "__main__":
>>>>>>> f66d6a3bcf2e29f70ec31c37d6af56ffbc6ddbf4
    app.run(debug=True)