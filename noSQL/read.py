from flask import Blueprint, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

# 定義 Blueprint
read_bp = Blueprint('read_bp', __name__)

# MongoDB connection (adjust as per your local MongoDB setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # The database name
collection = db['users']  # The collection name for users

@read_bp.route('/')
def index():
    # 從 MongoDB 中獲取所有用戶
    users = list(collection.find())

    # 在獲取用戶時，可以選擇將 _id 轉換為字符串，以便於顯示
    for user in users:
        user['_id'] = str(user['_id'])

    # Render the posts with the add/delete functionality
    return render_template('index.html', users=users)

