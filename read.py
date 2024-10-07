from flask import Blueprint, render_template
import mysql.connector

# 定義 Blueprint
read_bp = Blueprint('read_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'db'
}

@read_bp.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    select_query = "SELECT * FROM users"
    cursor.execute(select_query)
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the posts with the add/delete functionality
    return render_template('index.html', users=users)
