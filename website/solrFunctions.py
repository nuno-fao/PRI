import pysolr


def buildString(field, input, tags, minPrice, maxPrice, languages, publisher, developer, sort):
    # Example: **{'fq':'desc_snippet:dlc', 'sort':'original_price asc'}
    if minPrice == None:
        minPrice = 0
    if maxPrice == None:
        maxPrice = 100

    res = ""
    res = res + addPrice(minPrice, maxPrice)
    res = res + addTagsFilter(tags)
    res = res + addLanguagesFilter(languages)
    res = res + addPublisherFilter(publisher)
    res = res + addDeveloperFilter(developer)

    if sort == None :
        return (addSearchField(field, input), {'fq':res, 'sort':"all_reviews desc"})
    else:
        return (addSearchField(field, input), {'fq':res, 'sort':"original_price " + sort + " , all_reviews desc"})


def addSearchField(field, input):
    res = ""
    if field == 0:
        res = "name:" + "\""+ str(input) + "\"~1"
    elif field == 1:
        res = "game_description:" + "\""+ input + "\"~1"
    elif field == 2:
        res = "name:" + "\""+ input + "\"~1" + " OR " + "game_description:" + "\""+ input + "\"~1"
    elif field == 3:
        res = "reviews:" + "\""+ input + "\"~3"
    elif field == 4:
        res = "mature_content:" + "\""+ input + "\"~1"
    elif field == 5:
        res = "name:" + "\""+ input + "\"~1" + " OR " + "game_description:" + "\""+ input + "\"~1" + " OR " + "reviews:" + "\""+ input + "\"~1"

    return res    


def addTagsFilter(tags):
    res = ""
    if tags == "" or tags is None:
        return ""
    res = res + " AND "
    tagList = list(tags.split(","))
    for x in tagList[:-1]:
        res = res + "popular_tags:"+ "\""+ x + "\""+ " AND "
    else:
        res = res + "popular_tags:"+ "\""+ tagList[-1] + "\""
    return res

def addLanguagesFilter(languages):
    res = ""
    if languages == "" or languages is None:
        return ""
    print(languages)
    res = res + " AND "
    languageList = list(languages.split(","))
    for x in languageList[:-1]:
        res = res + "languages:"+ "\""+ x + "\""+ " AND "
    else:
        res = res + "languages:"+ "\""+ languageList[-1] + "\""
    return res

def addPublisherFilter(publisher):
    res = ""
    if publisher == "" or publisher is None:
        return ""
    res = res + " AND "
    publisherList = list(publisher.split(","))
    for x in publisherList[:-1]:
        res = res + "publisher:"+ "\"" + x + "\""+ " AND "
    else:
        res = res + "publisher:"+ "\"" + publisherList[-1] + "\""
    return res



def addDeveloperFilter(developer):
    res = ""
    if developer == "" or developer is None:
        return ""
    res = res + " AND "
    developerList = list(developer.split(","))
    for x in developerList[:-1]:
        res = res + "developer:"+ "\""+ x + "\""+ " AND "
    else:
        res = res + "developer:"+ "\""+ developerList[-1]+ "\""
    return res



def addPrice(minPrice, maxPrice):
    res = ""
    return "original_price:["+ str(minPrice) + " TO " + str(maxPrice) + "]"


def getGame(id):
    return solr.search('app_id:'+str(id))



# solr = pysolr.Solr('http://localhost:8983/solr/steam_test', always_commit=True)
# # solr.ping()
# # print(addTagsFilter(""))
# res = buildString(0, "Doom","",0, 999,"", "", "", "asc")
# # res = searchByName("doom", "asc")
# print(res)
# results = solr.search(res[0], **res[1])

# for result in results:
#     print(result["name"])



