from flask import Flask, render_template, request
from forms import BmForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'braunHeightsTools'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/newbm', methods=['GET', 'POST'])
def newbm():
    form = BmForm()
    return render_template("newbm.html", form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

