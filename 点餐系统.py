import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# 配置日志输出
logging.basicConfig(level=logging.DEBUG)  # 设置日志级别为 DEBUG

# 处理点餐请求
@app.route('/order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        order = request.json.get('order')  # 可以从请求中获取点餐信息
        total_amount = order.get('totalAmount')

        # 添加日志输出
        app.logger.debug('Received order: %s', order)

        # 处理订单逻辑，如保存订单到数据库等

        # 返回响应
        response_data = {'message': f'订单已提交，总金额为{total_amount}元'}
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