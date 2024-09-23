from flask import Blueprint, request, redirect, url_for, render_template
import mysql.connector

# 定義 Blueprint，命名為 create_bp
create_bp = Blueprint('create_bp', __name__)

# 資料庫配置
db_config = {
    'user': 'root',
    'password': 'password',  # 記得填寫正確的密碼
    'host': 'localhost',
    'database': 'db'
}

# 添加數據
@create_bp.route('/add', methods=['POST'])
def add_post():
    post_content = request.form.get('post', None)
    name = request.form.get('name', None)

    if post_content and name:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        insert_query = "INSERT INTO users (name, post) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, post_content))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        return "Name and post content required", 400

# 查找數據
@create_bp.route('/search', methods=['POST'])
def search_user():
    search_name = request.form.get('name', None)
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # 使用 LIKE 查找對應的 name
    search_query = "SELECT * FROM users WHERE name LIKE %s"
    cursor.execute(search_query, (f"%{search_name}%",))
    search_results = cursor.fetchall()

    cursor.close()
    conn.close()

    # 傳遞搜尋結果到 index.html
    return render_template('index.html', users=get_all_users(), search_results=search_results)

@create_bp.route('/delete', methods=['POST'])
def delete_user():
    name = request.form.get('name', None)

    if name:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 刪除對應 name 的數據
        delete_query = "DELETE FROM users WHERE name = %s"
        cursor.execute(delete_query, (name,))
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('index'))

def get_all_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
