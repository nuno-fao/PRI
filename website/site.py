from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")  # this sets the route to this page
def home():
	return redirect(url_for('search'))

@app.route("/search")  # this sets the route to this page
def search():
	return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)