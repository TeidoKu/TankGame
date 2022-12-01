from flask import Flask, render_template, request
import json
from models.player import Player

from flask import Flask
app = Flask(__name__)

data = Player().short_sort_by_time() # This is the data from the json file
fastest_p1 = Player().short_sort_by_time("P1")[0] # This is the fastest p1
fastest_p2 = Player().short_sort_by_time("P2")[0] # This is the fastest p2
sort_reqest_P1 = None #initializing sort requests
sort_reqest_P2 = None #initializing sort requests
@app.route("/" , methods=['GET'])
def home():
    sort_reqest_P1 = request.args.get('P1')
    sort_reqest_P2 = request.args.get('P2')
    

    if sort_reqest_P1 != None:
        scoreboard = Player().short_sort_by_time("P1")
    elif sort_reqest_P2 != None:
        scoreboard = Player().short_sort_by_time("P2")
    else:
        scoreboard = Player().short_sort_by_time(None)


    return render_template("home.html", scoreboard=scoreboard, fP1= fastest_p1,fP2 = fastest_p2),200


if __name__ == "__main__":
    app.run(debug=True)