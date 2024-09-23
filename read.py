from flask import Flask, render_template
import mysql.connector
from create import create_bp  # 引入 create_bp 藍圖

# 初始化 Flask 應用
app = Flask(__name__)
app.register_blueprint(create_bp)

# 資料庫配置
db_config = {
    'user': 'root',
    'password': 'password',  # 記得填寫正確的密碼
    'host': 'localhost',
    'database': 'db'
}

# 根路由，顯示所有資料
@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
