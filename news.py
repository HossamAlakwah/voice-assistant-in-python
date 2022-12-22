import requests
from api import *

#http://newsapi.org/v2/top-headlines?country=us&apiKey=5c6c5ff6326944458f307d6ae026e3e4

api_add="http://newsapi.org/v2/top-headlines?country=us&apiKey=" + news_key
json_data=requests.get(api_add).json()

ar=[]

def news():
    for i in range (3):
        ar.append("article "+str(i+1)+": "+json_data["articles"][i]["title"]+".")
    return ar

