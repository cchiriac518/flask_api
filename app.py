from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the API"
@app.route('/hostname')
def index2():
    return "Welcome to the API2"

if __name__ == '__main__':
    app.run(debug=True)