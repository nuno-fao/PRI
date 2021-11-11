#!/bin/bash

#Assumes existance of file steam_games.csv in the current dir
#https://www.kaggle.com/trolukovich/steam-games-complete-dataset - Please download this dataset


#create virtual environment and install requirements
venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt


run: venv/bin/activate

#dataset cleanup
	./venv/bin/python3 data_prep.py 

#scrape reviews from Steam website
	./venv/bin/python3 review_scraping.py

#simple regex to ensure json file validity
	sed -i 's/\]\[/,/g' reviews.json


#cleanup
clean:
	rm -rf __pycache__
	rm -rf venv
	rm temp.json