from flask import Flask, render_template, url_for, flash, redirect
from forms import UserText
import hashlib

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f257b1a89bfd0b413d012d079e03d12a'

@app.route("/", methods=['GET', 'POST'])
@app.route("/encrypt", methods=['GET', 'POST'])
def encyption():
    form = UserText()
    if form.validate_on_submit():
        msg = hashlib.sha256(bytes(form.text.data, encoding='utf-8'))
        encMsg = msg.hexdigest()
        flash(f'{encMsg}', 'success')
    return render_template("encrypt.html", title='Encrypt', form=form)

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(host='10.0.0.133', debug=True)
