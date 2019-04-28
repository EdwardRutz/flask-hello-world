from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)  # codeanywhere settings
    # app.run()   # Flask default runs on local host 127.0.0.1, port 5000
