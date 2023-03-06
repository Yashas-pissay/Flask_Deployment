from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "This is Our first flask deployment"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)