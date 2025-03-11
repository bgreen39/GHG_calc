from flask import flask
app = Flask (__name__)

@app.route("/")
def home():
  return "Brianna's GHG Calculator! :D"
