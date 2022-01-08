import pysolr

def searchByName(name):
    # Example: **{'fq':'desc_snippet:dlc', 'sort':'original_price asc'}
    return 'name:' + name


def searchByDescription(description):
    return solr.search('description:' + description)


def searchByReviews(reviews):
    return solr.search('reviews:' + reviews)

# solr = pysolr.Solr('http://localhost:8983/solr/steam_test', always_commit=True)
# solr.ping()

# results = searchByName("doom")

# for result in results:
#     print(result['name'])



