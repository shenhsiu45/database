from flask import Blueprint, request, render_template
from pymongo import MongoClient

# 定義 Blueprint
search_bp = Blueprint('search_bp', __name__)

# MongoDB connection (adjust as per your local MongoDB setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['local']  # The database name
collection = db['users']  # The collection name for users

# 搜索用户的路由
@search_bp.route('/search', methods=['GET'])
def search_user():
    search_query = request.args.get('query', '')  # 从URL中获取搜索查询参数

    # 使用正则表达式进行模糊搜索
    search_results = list(collection.find({'name': {'$regex': search_query, '$options': 'i'}}))

    # 转换 _id 为字符串以便于显示
    for user in search_results:
        user['_id'] = str(user['_id'])

    # 渲染包含搜索结果的页面
    return render_template('index.html', users=search_results)
