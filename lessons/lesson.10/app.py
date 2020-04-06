from flask import Flask, request, jsonify, render_template

from product_views import product_app

app = Flask(__name__)
app.register_blueprint(product_app, url_prefix='/product')


@app.route('/', methods=('GET', 'POST', 'PUT'))
def index():
    if request.method == 'GET':
        return render_template('index.html', name=request.args.get('name'))
        # return '''
        # <title>Index</title>
        # <h1>Hello world!</h1>
        # '''
    return jsonify(method=request.method, result='created', **request.json)


@app.route('/check/<int:data>')
@app.route('/check/<float:data>')
@app.route('/check/<string:data>')
def check_data(data):
    print(type(data))
    return f'<code>{data}</code>'


if __name__ == '__main__':
    app.run(debug=True)
