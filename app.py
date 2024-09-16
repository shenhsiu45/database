from flask import Flask, render_template, request, redirect
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
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM users")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def insert_data_to_db(name):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 獲取用戶輸入的名字並插入資料庫
        name = request.form['name']
        if name:
            insert_data_to_db(name)
        return redirect('/')  # 插入後重定向回首頁以更新顯示的資料
    
    # 顯示資料庫中的用戶
    users = get_data_from_db()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
