from flask import Flask, render_template
import requests
import json

BASE_URL="https://data.artmuseum.princeton.edu"
OBJECTS="/objects/"

app = Flask(__name__)

def getJSON(endpoint, **params):
    req = requests.get(
        BASE_URL + endpoint,
        params=params,
    )

    if req.ok:
        return req.json()
    else:
        return req.text

@app.route("/")
def index():
	# load current count
	f = open("count.txt", "r")
	count = int(f.read())
	f.close()

	count += 1

	f = open("count.txt", "w")
	f.write(str(count))
	f.close()

	objectid = 25277

	endpoint = OBJECTS + str(objectid)

	objects = getJSON(endpoint)
	print(objects)

	return render_template("index.html", count=count, objectName=objects['titles'][0]['title'])



if __name__ == "__main__":
	app.run()