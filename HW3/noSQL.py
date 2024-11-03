from flask import Flask, render_template
from pymongo import MongoClient

from create import create_bp
from read import read_bp
from delete import delete_bp
from update import update_bp
from search import search_bp

app = Flask(__name__)

# MongoDB connection (adjust as per your local MongoDB setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # The database name
collection = db['users']  # The collection name

# Register blueprints
app.register_blueprint(create_bp)
app.register_blueprint(read_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(update_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True) 