from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/dingtalk',methods=['post'])
def handle_receive_message():
    data=request.get_jason()
    return jsonify(),200

if __name__=="__main__":
    app.run(host='0.0.0.0',port=9527)
    