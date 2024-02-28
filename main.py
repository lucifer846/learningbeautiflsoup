from bs4 import BeautifulSoup

with open("index.html") as f:
    doc = BeautifulSoup(f, "html.parser")

find = doc.find_all("p")
print(find[0].find_all("b"))