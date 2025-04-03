from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route('/index.html')
@app.route('/index.htm')
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/donations')
def donations():
    return app.redirect(location='/#donation', code=302)

@app.route('/thanks/maiapp')
def donations():
    return render_template('thanks/maiapp.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
