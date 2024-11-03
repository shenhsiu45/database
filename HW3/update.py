from flask import Blueprint, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId  # MongoDB ObjectId

# 定義 Blueprint
update_bp = Blueprint('update_bp', __name__)

# MongoDB connection (調整為您的 MongoDB 設定)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # 資料庫名稱
collection = db['users']  # 集合名稱

# 更新用戶的路由
@update_bp.route('/update/<user_id>', methods=['POST'])
def update_user(user_id):
    # 獲取表單中的所有字段
    form_data = request.form.to_dict()
    
    # 提取用戶的名字
    new_name = form_data.get(f'name_{user_id}')
    
    # 檢查是否有輸入新名字
    if not new_name:
        return "No name provided", 400
    
    # 更新用戶名字
    result = collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': {'name': new_name}}
    )
    
    # 檢查更新是否成功
    if result.matched_count == 0:
        return "User not found", 404

    return redirect(url_for('read_bp.index'))  # 重定向到首頁

