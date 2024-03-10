from bs4 import BeautifulSoup
import requests
import sys,io

#set the console encoding to utf-8 to display the indian rupee sign in webpage
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = "https://coinmarketcap.com/"

fetch = requests.get(url)
soup = BeautifulSoup(fetch.text, "html.parser")
tbody = soup.find("tbody")
trows = tbody.find_all("tr")

for i in trows:
    tagwithname = i.find("div", class_="sc-a0353bbc-0 gDrtaY")
    price = tagwithname.text
    print(price)
#this code doesnt' work anymore , i think its due to the autochange in class name 