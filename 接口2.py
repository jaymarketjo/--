from flask import Flask,jsonify,send_file

app=Flask(__name__)

#普通的文本接口
@app.route('/text')
def text():
    return'您正在访问Python写的接口!!!'

#JSON数据返回接口
@app.route('/json')
def return_json():
    data={'msg':'This is a json RESPONSE'}
    return jsonify(data)

#图片返回接口
@app.rute('/image')
def return_image():
    image_path='D:\Fan\运维\PLM\飞渡PLM实施\培训图片签到表\现场图片'
    return send_file{image_path,mimetype='image/jpeg'}

#app.run  启动接口
if __name__=='_main_'
 app.run(host='0.0.0.0',port=5004)

 #flask重定向
 @app.route('/baidu')
 def baidu():
    return redirect("https://www.baidu.com")
    