import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# import blueprints
from _code.blueprints.banking_system import bankingsystem
from _code.blueprints.shipping_system import shippingsystem

# register blueprints
app.register_blueprint(bankingsystem)
app.register_blueprint(shippingsystem)


@app.route('/')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()