from flask import Blueprint, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

update_bp = Blueprint('update_bp', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['local']
collection = db['users']

@update_bp.route('/update/<user_id>', methods=['POST'])
def update_user(user_id):
    form_data = request.form.to_dict()
    
    # 獲取 name 和 age 欄位
    new_name = form_data.get(f'name_{user_id}')
    new_age = form_data.get(f'age_{user_id}')  # 新增 age 欄位

    # 檢查是否有輸入新名字
    if not new_name or not new_age:
        return "Name or age not provided", 400
    
    # 更新用戶名字和年齡
    result = collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': {'name': new_name, 'age': int(new_age)}}
    )
    
    if result.matched_count == 0:
        return "User not found", 404

    return redirect(url_for('read_bp.index'))
