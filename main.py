from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route('/index.html')
@app.route('/index.htm')
@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
