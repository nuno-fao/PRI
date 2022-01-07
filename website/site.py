from flask import Flask, redirect, url_for, render_template, request
import requestAPI
from requestAPI import RequestAPI
import json

app = Flask(__name__)

# Uncomment if solr is opened
# request_api = RequestAPI()
# request_api.open(url='http://localhost:8983/solr/steam')

@app.route("/")  # this sets the route to this page
def home():
	return redirect(url_for('search'))

@app.route("/search", methods=["GET"])  # this sets the route to this page
def search():
	return render_template("search.html")

@app.route("/results", methods=["GET"])
def results():
	text = request.args["text"]
	field = request.args["field"]

	maxprice = request.args.get("maxprice")
	if maxprice==999: maxprice=None
	minprice = request.args.get("minprice")
	if minprice==0: minprice=None

	tags = request.args.get("tags")
	developer = request.args.get("developer")
	publisher = request.args.get("publisher")
	languages = request.args.get("tags")

	sortby = request.args.get("pricesort")
	if sortby == "None": sortby=None

	#query solr and pass the results to the results page with text and field retrieved from search page
	#put the results in games variable, should be a list of games

	games = []

	return render_template("results.html", games=games, length=len(games), querytext=text, queryfield=field)


if __name__ == "__main__":
    app.run(debug=True)