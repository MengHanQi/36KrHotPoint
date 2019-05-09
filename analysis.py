import csv
from collections import defaultdict

def get_company():
    fp =  open("大型公司.txt")
    companies = []
    for line in fp:
        line = line.strip()
        companies.append(line)
    return companies

def get_place():
    places = []
    fp = open("省份+国家.txt")
    for line in fp:
        place = line.strip()
        places.append(place)
    return places

def read_data():
    fp = open("result.csv", newline='', encoding="utf-8-sig")
    reader = csv.DictReader(fp)
    data_lst = []
    for row in reader:
        data_lst.append(row)
    return data_lst

def get_company_occur_count(data_lst, companies):
    freq = {}
    for data in data_lst:
        title = data["title"]
        for company in companies:
            if company in title:
                if company not in freq:
                    freq[company] = 1
                else:
                    freq[company] = freq[company] + 1
    return freq

def get_place_occur_count(data_lst, places):
    freq = {}
    for data in data_lst:
        title = data["title"]
        for place in places:
            if place in title:
                if place not in freq:
                    freq[place] = 1
                else:
                    freq[place] = freq[place] + 1
    return freq

def count_by_date(data_lst):
    freq = {}
    for data in data_lst:
        date = data["publish_time"]
        day = date.split()[0]
        if day not in freq:
            freq[day] = 1
        else:
            freq[day] = freq[day] + 1
    return freq

