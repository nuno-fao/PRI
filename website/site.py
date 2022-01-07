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

@app.route("/results", methods=["GET", "POST"])
def results():
	if request.method=='GET':
		text = request.args["text"]
		field = request.args["field"]
		
		#query solr and pass the results to the results page with text and field retrieved from search page
		#put the results in games variable, should be a list of games

		games = []

		return render_template("results.html", games=games, length=len(games))


if __name__ == "__main__":
    app.run(debug=True)