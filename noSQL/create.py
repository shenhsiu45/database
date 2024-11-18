from flask import Blueprint, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

# 定义 Blueprint
create_bp = Blueprint('create_bp', __name__)

# MongoDB connection (根据您的本地 MongoDB 设置进行调整)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # 数据库名称
collection = db['users']  # 集合名称

# 新增数据的路由
@create_bp.route('/add', methods=['POST'])
def add_user():
    # 从表单获取 name 和 age 数据
    name = request.form.get('name')
    age = request.form.get('age')

    # 检查 name 和 age 是否提供
    if name and age:
        # 获取当前时间
        submission_time = datetime.now()

        # 插入到 MongoDB
        collection.insert_one({
            'name': name,
            'age': int(age),  # 将年龄转换为整数类型存储
            'created_at': submission_time
        })

    return redirect(url_for('read_bp.index'))
