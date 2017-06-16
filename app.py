from flask import Flask, request, redirect, url_for, render_template
from feedback import FeedbackForm
import os


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS') or 'config.DevelopmentConfig')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/feedback", methods=["GET", "POST"])
def set_data():
    form = FeedbackForm(request.form)
    if form.validate_on_submit():
        response = redirect(url_for("hello"))
        response.set_cookie("test", "blah")
        return response
    return render_template('index.html', form=form)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    app.run(host='0.0.0.0')
