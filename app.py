from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL 資料庫連接設置
db_config = {
    'user': 'root',  # 替換為你的 MySQL 資料庫用戶名
    'password': 'password',  # 替換為你的 MySQL 資料庫密碼
    'host': 'localhost',  # 如果 MySQL 服務器在本地運行
    'database': 'db'  # 資料庫名稱
}

def get_data_from_db():
    # 連接 MySQL
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # 假設資料庫有一個 'users' 表
    cursor.execute("SELECT id, name FROM users")
    result = cursor.fetchall()

    # 關閉連接
    cursor.close()
    connection.close()

    return result

@app.route('/')
def index():
    users = get_data_from_db()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
