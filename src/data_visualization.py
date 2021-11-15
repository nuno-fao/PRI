import pandas as pd
import json
import matplotlib.pyplot as plt
from operator import itemgetter
import collections



def months():
    with open('files/months.json') as months:
        data = json.load(months)


    labels = list(data.keys())

    values = list(data.values())

    # Plot
    plt.pie(values, labels=labels, autopct='%1.0f%%')
    # plt.bar(list(labels), list(values))

    plt.axis('equal')
    plt.show()

def genres():
    with open('files/genres.json') as genres:
        data = json.load(genres)
    


    res = dict(sorted(data.items(), key = itemgetter(1), reverse = True)[:15])
    other = dict(sorted(data.items(), key = itemgetter(1), reverse = True)[15:])


    othervalues = list(other.values())


    sumOther = 0
    for x in othervalues:
        sumOther += x
    print(sumOther)


    res["other"] = sumOther
    labels = list(res.keys())
    values = list(res.values())

    plt.pie(values, labels=labels, autopct='%1.0f%%')
    plt.show()

    


def prices():
    with open('files/prices.json') as prices:
        data = json.load(prices)

    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize = (10, 5))

    plt.bar(keys, values, width=0.4)
    plt.xlabel("Game Price")
    plt.ylabel("No. of games")
    plt.show()


def prices():
    with open('files/prices.json') as prices:
        data = json.load(prices)

    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize = (10, 5))

    plt.bar(keys, values, width=0.4)
    plt.xlabel("Game Price")
    plt.ylabel("No. of games")
    plt.show()

def reviews():
    with open('files/reviewsDistribution.json') as reviews:
        data = json.load(reviews)

    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize = (10, 5))

    plt.bar(keys, values, width=0.4)
    plt.show()

def years():
    with open('files/years.json') as years:
        data = json.load(years)


    data = {int(k):int(v) for k,v in data.items()}


    data = collections.OrderedDict(sorted(data.items()))

    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize = (10, 5))
    plt.plot(keys, values)
    plt.xlabel("Year")
    plt.ylabel("No. of games released")
    plt.xlim([1985, 2020])
    plt.show()


genres()
months()
prices()
reviews()
years()