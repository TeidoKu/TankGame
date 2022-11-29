from flask import Flask, render_template, request
import json

from flask import Flask
app = Flask(__name__)

with open('../data/record.json') as json_file:
    data = json.load(json_file)

@app.route("/")
def home():
    scoreboard = data
    return render_template("home.html", scoreboard=scoreboard),200

if __name__ == "__main__":
    app.run(debug=True)