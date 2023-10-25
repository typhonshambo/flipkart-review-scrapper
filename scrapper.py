import requests
from bs4 import BeautifulSoup
import json

def error_handler(response):
    if response.status_code != 200:
        print(f"Error: Unable to fetch data. Status code {response.status_code}")
        return True
    return False

def scraper(keyword):
    url = "https://www.flipkart.com/search?q="
    r = requests.get(url + keyword)
    
    if error_handler(r):
        return
    
    pageSource = r.text
    soup = BeautifulSoup(pageSource, "html.parser")
    box = soup.findAll("div", {"class": "_13oc-S"})
    title = (soup.findAll("div", {"class": "CXW8mj"}))
    links = []
    headings = []

    # product titles
    for i in title:
        val = i.img['alt']
        headings.append(val)

    # getting product links
    for i in box:
        val = i.div.div.a['href']
        links.append(val)

    datas = []

    # getting reviews
    print("loading...")
    for j in range(0, len(links)):
        r = requests.get("https://www.flipkart.com" + links[j])
        if error_handler(r):
            continue
        
        pageSource = r.text
        soup = BeautifulSoup(pageSource, "html.parser")
        box = soup.findAll("div", {"class": "t-ZTKy"})

        reviews = []
        for i in box:
            val = (i.div.div).text
            reviews.append(val)

        data = {
            f"{headings[j]}": reviews
        }
        datas.append(data)

    with open("data.json", "w") as f:
        json.dump(datas, f)

    print("Done check data.json")

