import requests
import json

apitokennewsapi = ""

author = []
title = []
desc = []

def getAPI(api):
    global apitokennewsapi
    apitokennewsapi = api

def getNews(sources="bbc-news"):
    response = requests.get('http://newsapi.org/v2/top-headlines?sources='+sources+'&apiKey='+apitokennewsapi)
    return response
    
def headlines(maxResult="5"):
    author = []
    title = []
    desc = []

    number = 0
    
    response = getNews(sources="bbc-news")
    newsRaw = response.json()["articles"]

    for imp in newsRaw:
        if (maxResult >= number):
            number = number + 1
            author.append(imp["author"])
            title.append(imp["title"])
            desc.append(imp["description"])

    search = {
        "author": author,
        "title": title,
        "desc": desc
    }
    final = json.dumps(search)

    return final
