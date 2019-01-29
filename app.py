from flask import (Flask ,request, url_for, abort, redirect,
                    make_response, session, render_template, render_template_string)
app = Flask(__name__)
app.secret_key = 'kdjfkdjf#%$FfdsfafeTRT$#%#$46546'

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


@app.route('/statictest')
def statictest():
    url = url_for("static",filename='ppp.jpg')
    return '<img src="%s" />' % url

@app.route('/redirect')
def redirecttest():
    return abort(404)
    # return redirect(url_for('index'))

@app.errorhandler(404)
def ff(error):
    return 'err',404

@app.route('/resp_test')
def resp_test():
    resp = make_response('aaaaaaaaaa', 200)
    resp.headers['X-Something'] = 'Avvvv'
    return resp

@app.route('/cookie_test')
def cookie_test():
    resp = make_response('set cookie', 200)
    resp.set_cookie('username','dddc')
    return resp

@app.route('/cookie_test2')
def resp_test2():
    resp = make_response('set cookie', 200)
    if request.cookies.get('username'):
        resp.set_cookie('username',request.cookies.get('username')+'a')
    else:
        resp.set_cookie('username','dddc')
    return resp

@app.route('/session_test')
def session_test():
    if 'username' in session:
        print(session['username'])
    else:
        session['username'] = 'name_in_session'
    return 'session_test'

@app.route('/temp_test')
def temp_test():
    name = 'abc'
    return render_template_string('Hello {{name}}!', name=name)

@app.route('/tempfile_test')
def tempfile_test():
    name = 'abc'
    return render_template('index.html', name=name)
