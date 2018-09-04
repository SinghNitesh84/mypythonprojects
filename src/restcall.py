from flask import Flask,request,render_template
import requests
app = Flask(__name__)

@app.route("/pythonpoc/<username>")
def adlookup(username):
    return ("HELLO WORLD")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
