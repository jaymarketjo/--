from flask import Flask
app=Flask(__name__)
@app.route('/good')
def good():
    return'goodday'
if __name__=='_main_':
    app.run(host='0.0.0.0', port=5001)
    