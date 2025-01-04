from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟用户数据
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 30},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 28}
]

# 获取特定用户信息的API接口
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# 创建新用户的API接口
@app.route('/api/user', methods=['POST'])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/good')
def good():
    return'goodday'

if __name__ == '__main__':
    app.run(debug=True)
