import logging
from flask import Flask, request, jsonify
from flask_cors import CORS  # 导入 CORS 扩展
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # 添加 CORS 支持

# 配置日志输出
logging.basicConfig(level=logging.DEBUG)  # 设置日志级别为 DEBUG

# 连接 MongoDB 数据库
client = MongoClient('mongodb://localhost:27017/')
db = client['order_database']
orders_collection = db['orders']

# 处理点餐请求
@app.route('/order', methods=['POST'])
def place_order():
    if request.method == 'POST':
        order = request.json  # 获取前端发送的全部订单数据
        if order is None:
            return jsonify({'message': '订单信息为空'})

        # 添加日志输出
        app.logger.debug('Received order: %s', order)

        # 将订单信息存储到数据库
        orders_collection.insert_one(order)

        # 打印订单信息
        app.logger.info('订单信息已存储：%s', order)

        # 返回响应
        response_data = {'message': '订单已提交'}
        app.logger.debug('Response  %s', response_data)
        return jsonify(response_data)
    else:
        return jsonify({'message': '请使用 POST 方法提交订单'})

# 设置静态文件目录
@app.route('/')
def index():
    return app.send_static_file('index.html')

# 启动服务器
if __name__ == '__main__':
    app.run(debug=True)