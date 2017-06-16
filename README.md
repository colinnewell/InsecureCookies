# Insecure Cookies

This is a really simple 2 page site demonstrating how
badly put together crypto can fall apart.

http://localhost:5000/

On the feedback page you can enter some text that will
be stored encrypted in a cookie and then shown on the root
page.

http://localhost:5000/feedback

### Running

    python app.py

### Setup

Assumes Ubuntu (probably works for other Debian variants too)

    apt-get install python3-dev python3-virtualenv
    virtualenv --python `which python3` env
    source env/bin/activate
    pip install -r requirements.txt

