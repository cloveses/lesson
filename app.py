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

@app.route('/posttest', methods=['GET','POST'])
def posttest():
    if request.method == 'GET':
        return '<form method="post"><input name="name" type="text"><input type="submit"></form>'
    elif request.method == 'POST':
        print(request.form['name'])
        return 'aa'