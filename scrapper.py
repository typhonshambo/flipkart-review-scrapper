import requests
from bs4 import BeautifulSoup
import json


def scraper(keyword):
    url = "https://www.flipkart.com/search?q="
    r = requests.get(url + keyword)
    pageSource = r.text
    soup = BeautifulSoup(pageSource, "html.parser")
    box = soup.findAll("div", {"class": "_13oc-S"})
    title = soup.findAll("div", {"class": "CXW8mj"})
    links = []
    headings = []

    # product titles
    for i in title:
        val = i.img['alt']
        headings.append(val)

    datas = []  # Initialize an empty list for storing product entries

    # getting product links
    for i in box:
        val = i.div.div.a['href']
        links.append(val)

    # getting reviews
    print("loading...")
    for j in range(0, len(links)):
        r = requests.get("https://www.flipkart.com" + links[j])
        pageSource = r.text
        soup = BeautifulSoup(pageSource, "html.parser")
        box = soup.findAll("div", {"class": "t-ZTKy"})

        reviews = []
        for i in box:
            val = (i.div.div).text
            reviews.append(val)

        # Create a product entry as a dictionary
        product_entry = {
            "product_name": headings[j],
            "reviews": reviews
        }
        datas.append(product_entry)  # Append the product entry to the list

    with open("data.json", "w") as f:
        json.dump(datas, f, indent=4)  # Dump the list of product entries to the JSON file

    print("Done, check data.json")

