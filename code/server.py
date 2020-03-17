from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")


@app.route('/newbm')
def newbm():
    return render_template("newbm.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')

