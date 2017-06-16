from flask import Flask
from feedback import FeedbackForm


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/feedback", methods=["GET", "POST"])
def set_data():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        response = redirect(url_for("hello"))
        response.set_cookie("test", "blah")
        return response
    return render_template('index.html', form=form)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    app.run(host='0.0.0.0')
