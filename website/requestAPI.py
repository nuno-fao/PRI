import pysolr
import json

class RequestAPI:

    def open(self, url):
        self.solr = pysolr.Solr(url, always_commit=True)
        # Create a client instance. The timeout and authentication options are not required.
    

        # Note that auto_commit defaults to False for performance. You can set
        # `auto_commit=True` to have commands always update the index immediately, make
        # an update call with `commit=True`, or use Solr's `autoCommit` / `commitWithin`
        # to have your data be committed following a particular policy.

        # Do a health check.
        self.solr.ping() 
    
    def load(self):
        f = open('steam_games_prep.json')
        self.solr.add(json.load(f))