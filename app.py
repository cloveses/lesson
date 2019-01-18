from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Flask</h1>"

@app.route('/gtest')
def gettest():
    print(request.args.get('name',''))
    print(request.args['name'])
    return 'success!'

@app.route('/ptest', methods=['GET','POST'])
def posttest():
    if request.method == 'GET':
        return '<form method="post"><input name="name" type="text"><input type="submit"></form>'
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form.get('sname','defaults'))
        return 'aa'

@app.errorhandler(404)
def ff(error):
    return 'err',404