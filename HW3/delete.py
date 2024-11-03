from flask import Blueprint, request, redirect, url_for
from pymongo import MongoClient

# 定義 Blueprint
delete_bp = Blueprint('delete_bp', __name__)

# MongoDB connection (adjust as per your local MongoDB setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # The database name
collection = db['users']  # The collection name for users

@delete_bp.route('/delete', methods=['POST'])
def delete_user():
    user_ids = request.form.getlist('user_ids')  # 獲取所有選中的用戶ID

    if user_ids:
        # 將用戶 ID 轉換為 ObjectId 格式，因為 MongoDB 中的 ID 通常是 ObjectId
        from bson.objectid import ObjectId

        # 刪除所有選中的用戶
        collection.delete_many({'_id': {'$in': [ObjectId(user_id) for user_id in user_ids]}})

    return redirect(url_for('read_bp.index'))  # 返回到用戶列表頁面
