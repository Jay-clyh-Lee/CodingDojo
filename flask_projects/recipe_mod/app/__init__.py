from flask import Flask

app = Flask(__name__)

app.secret_key = "do not tell anyone about this secret key."