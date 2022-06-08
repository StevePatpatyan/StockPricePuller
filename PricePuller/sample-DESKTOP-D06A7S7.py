from bs4 import BeautifulSoup
import requests
htmlText = requests.get("https://www.freecatphotoapp.com/").text
soup = BeautifulSoup(htmlText,'lxml')
body = soup.findAll('a', href_=True)
print(body)
