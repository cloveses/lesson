from flask import Flask ,request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Flask</h1>"

@app.route('/index/<float:uid>', methods=['GET','POST'])
def indexp(uid):
    if request.method == 'GET':
        print(type(uid))
        return 'hhh'
    else:
        return "<h1>Hello Flask</h1>"

@app.route('/gtest')
def gettest():
    print(request.args.get('name',''))
    # try:
    #     print(request.args['name'])
    # except KeyError as e:
    #     print('kkk')
    print(request.url)
    print(request.base_url)
    return 'success!'

@app.route('/ptest', methods=['GET','POST'])
def posttest():
    if request.method == 'GET':
        return '<form method="post"><input name="name" type="text"><input type="submit"></form>'
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form.get('sname','defaults'))
        return 'aa'

# @app.errorhandler(404)
# def ff(error):
#     return 'err',404