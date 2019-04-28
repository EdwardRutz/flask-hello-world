from flask import Flask

app = flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
