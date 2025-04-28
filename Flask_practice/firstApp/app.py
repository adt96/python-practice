from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/hello')
def hello():
    return '<h1>Hello, Flask!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
# This code creates a simple Flask application with two routes: '/' and '/hello'.
