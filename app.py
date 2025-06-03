from flask import Flask, jsonify, request, session, send_from_directory
from flask_session import Session
from dbutils.pooled_db import PooledDB
import os
import pymysql
import bcrypt
from flask_cors import CORS


POOL = PooledDB(
    creator=pymysql,
    maxconnections=5,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping = 0,
    host='127.0.0.1',  # 连接名称，默认127.0.0.1
    user='root',  # 用户名
    passwd='root',  # 密码
    port=3306,  # 端口，默认为3306
    db='test',  # 数据库名称
    charset='utf8mb4',  # 字符编码
)

app = Flask(__name__)
CORS(app,supports_credentials=True)  # 跨域支持
app.config['SECRET_KEY'] = 'BTJybk4hjV3c3FTbb7BY'  # 请替换为一个更安全的随机字符串


@app.route('/api/auth/register', methods=["POST"])
def register():
    print(request)
    resp = {}
    conn = POOL.connection()
    cursor = conn.cursor()
    name = request.get_json()['username']
    pwd = request.get_json()['password']
    # 查看用户是否存在
    cursor.execute("SELECT * FROM users WHERE username = %s", (name,))
    user = cursor.fetchone()

    if user:
        resp['msg'] = "用户已存在！"
        resp['status'] = "error"
    else:
        # 使用 bcrypt 或其他算法生成密码哈希
        hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
        # 插入新用户，存储哈希后的密码
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (name, hashed_pwd))
        resp['msg'] = "注册成功！"
        resp['status'] = "success"

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(resp)

@app.route("/api/auth/login", methods=["POST"])
def login():
    resp = {}
    conn = POOL.connection()
    cursor = conn.cursor()

    name = request.get_json()['username']
    pwd = request.get_json()['password']
    # 从数据库查询用户信息
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (name,))
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    user = cursor.fetchone()

    if user:
        stored_password = user[5]  # 假设第三列是密码
        # 验证密码是否匹配
        if bcrypt.checkpw(pwd.encode('utf-8'), stored_password.encode('utf-8')):
            session['user'] = user
            resp['status'] = "success"
        else:
            resp['status'] = "error"

    cursor.close()
    conn.close()
    return jsonify(resp)

@app.route('/api/auth/logout', methods=["POST"])
def logout():
    resp = {}
    session.pop('user', None)  # 清除 Session
    resp['status'] = "success"
    return jsonify(resp)


 

if __name__ == '__main__':
    # for rule in app.url_map.iter_rules():
    #     print(rule)
    app.run(
        host='0.0.0.0', 
        port=9999, debug=True,
        ssl_context=('./https/localhost.crt', 
                     './https/localhost.key')
                     
    )