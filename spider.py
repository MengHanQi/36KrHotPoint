import requests
import json
import csv
from bs4 import BeautifulSoup

def get_first_page(url, writer):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    data = soup.find_all(id="app")[0].find_next().text.strip("var props=")
    data = data.strip()
    index = data.find(",locationnal")
    data = json.loads(data[:index])
    news_lst = data["newsflashList|newsflash"]
    news_id = None
    for news in news_lst:
        news_id = news["id"]
        title = news["title"]
        description = news["description"]
        new_url = news["news_url"]
        publish_time = news["published_at"]
        writer.writerow({
            "id":news_id, "title":title, "description":description, 
            "news_url":new_url, "publish_time":publish_time
            })
    return news_id

def get_next_page(prev_id):
    url = "https://36kr.com/api/newsflash?b_id=%s&per_page=50" % prev_id
    res = requests.get(url)
    data = res.json()["data"]["items"]
    return data


def main():
    output = open("result.csv", "w", encoding="utf-8-sig", newline="")
    fields = ["id", "title", "description", "news_url", "publish_time"]
    writer = csv.DictWriter(output, fields)
    writer.writeheader()
    news_id = get_first_page("https://36kr.com/newsflashes", writer)
    for i in range(1,100):
        news_lst = get_next_page(news_id)
        for news in news_lst:
            news_id = news["id"]
            title = news["title"]
            description = news["description"]
            new_url = news["news_url"]
            publish_time = news["published_at"]
            writer.writerow({
                "id":news_id, "title":title, "description":description, 
                "news_url":new_url, "publish_time":publish_time
                })
    output.close()

import time
start = time.time()
main()
end = time.time()
print("cost %s" % (end-start))