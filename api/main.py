import flask
from flask import  jsonify

app = flask.Flask('__main__')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/linkk',methods=['GET','POST'])
def link():
    return jsonify({"key":"The Secret"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return flask.render_template("index.html")

app.run(debug=True)