import requests
from bs4 import BeautifulSoup
import argparse

word = "DD bag Maxwell & Gambhir, Dhoni returns to CSK"

r = requests.get('http://www.google.com/search',
                 params={'q':'"'+word+'"',
                         "tbs":"li:1"}
                )

soup = BeautifulSoup(r.text, "lxml")

results = soup.find('div',{'id':'resultStats'}).text

if(results == ""):
	print("wtf?")
else:
	print(results)