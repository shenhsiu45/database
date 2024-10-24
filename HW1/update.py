from flask import Blueprint, request, redirect, url_for
import mysql.connector

# 定義 Blueprint
update_bp = Blueprint('update_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'db'
}

# 更新用户的路由
@update_bp.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    # 获取新的用户名
    new_name = request.form.get('name')

    # 确保有内容需要更新
    if not new_name:
        return "No content to update", 400

    # 更新数据库中的用户名
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    update_query = "UPDATE users SET name = %s WHERE id = %s"
    cursor.execute(update_query, (new_name, user_id))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('read_bp.index'))  # 重定向到主页
