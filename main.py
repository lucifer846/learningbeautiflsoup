from bs4 import BeautifulSoup
import requests
import sys, io

#set the console encoding to utf-8 to display the indian rupee sign in webpage
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = "https://www.croma.com/phones-wearables/mobile-phones/android-phones/c/95"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

try:
    for i in range(100):
        rate = soup.find_all("li", class_="product-item")[i] # the li tags lists all products
        #print(rate.prettify())
        name = rate.find_all("a")[1].text
        price = rate.find("span", class_="amount plp-srp-new-amount").text
        print(name, price)
except IndexError:
    print(f"only {i} products available")