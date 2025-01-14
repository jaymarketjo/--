from flask import Flask # 导入Flask模块  #请备注每一句代码有什么用
app=Flask(__name__) # 创建一个Flask应用实例
@app.route('/good') # 定义一个路由，指定URL为/good
def good(): # 定义一个视图函数good
    return'goodday' # 当访问/good时，返回'goodday'
if __name__=='_main_': # 检查是否为主程序入口
    app.run(host='0.0.0.0', port=5001) # 在主程序入口时，运行Flask应用，监听所有网络接口，端口号为5001
    