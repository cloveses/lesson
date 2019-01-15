from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>rHello Flask</h1>"

@app.route('/gettest')
def gettest():
    print(request.args.get('sname',''))
    print(request.args['sname'])
    return 'success!'