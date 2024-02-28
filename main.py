from bs4 import BeautifulSoup
import requests
import sys, io

#set the console encoding to utf-8 to display the indian rupee sign in webpage
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = "https://www.croma.com/phones-wearables/mobile-phones/android-phones/c/95"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
print(soup.prettify())