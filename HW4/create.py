from flask import Blueprint, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

# 定義 Blueprint
create_bp = Blueprint('create_bp', __name__)

# MongoDB connection (adjust as per your local MongoDB setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # The database name
collection = db['users']  # The collection name

# 新增數據的路由
@create_bp.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')

    if name:
        # 獲取當前時間
        submission_time = datetime.now()

        # 插入到 MongoDB
        collection.insert_one({
            'name': name,
            'created_at': submission_time
        })

    return redirect(url_for('read_bp.index'))
