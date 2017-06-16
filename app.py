from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from feedback import FeedbackForm
from flask_bootstrap import Bootstrap
from flask import Flask, request, redirect, url_for, render_template, make_response
import os
import base64

app = Flask(__name__)
app.config.from_object(
    os.environ.get('APP_SETTINGS') or 'config.DevelopmentConfig')
Bootstrap(app)


@app.route("/")
def hello():
    feedback = request.cookies.get('test')
    if feedback:
        try:
            return decrypt(feedback)
        except Exception as e:
            return make_response("Error: {0}".format(e), 500)
    return "Hello World!"


@app.route("/feedback", methods=["GET", "POST"])
def set_data():
    form = FeedbackForm(request.form)
    if form.validate_on_submit():
        response = redirect(url_for("hello"))
        response.set_cookie("test", encrypt(form.feedback.data))
        return response
    return render_template('index.html', form=form)


def get_cipher(iv):
    backend = default_backend()
    key = app.config['KEY']
    return Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)


def encrypt(text):
    bytes = text.encode('utf-8')

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(bytes) + padder.finalize()

    iv = os.urandom(16)
    cipher = get_cipher(iv)
    encryptor = cipher.encryptor()
    ct = iv + encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(ct)


def decrypt(data):
    encoded = base64.b64decode(data)

    iv = encoded[:16]
    ct = encoded[16:]
    cipher = get_cipher(iv)
    decryptor = cipher.decryptor()
    padded = decryptor.update(ct) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    pt = unpadder.update(padded) + unpadder.finalize()

    return pt.decode('utf-8')


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    app.run(host='0.0.0.0')
