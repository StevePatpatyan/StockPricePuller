from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
stockName = input("Type a corp name to get its current stock price and rate of change. If the corp has multiple words, add a '+' between each word: ")
url = 'https://www.google.com/search?q='+stockName+'+stock&rlz=1C1CHBF_enUS923US923&oq='+stockName+'+stock&aqs=chrome..69i57j69i59j0i20i263i433i512j0i512l7.14204j1j7&sourceid=chrome&ie=UTF-8'
web = webdriver.Chrome()
web.get(url)
