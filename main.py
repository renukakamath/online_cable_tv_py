from flask import Flask
from public import public
from admin import admin
from musician import musician
from employer import employer
app=Flask(__name__)


app.secret_key="key"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(musician)
app.register_blueprint(employer)
app.run(debug=True,port=5049)