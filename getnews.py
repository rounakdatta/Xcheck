import requests
from bs4 import BeautifulSoup
import argparse

# ----google search it---

def google_search_it(query):
	r = requests.get("https://www.google.com/search", params={'q':query})

	soup = BeautifulSoup(r.text, "lxml")
	results = soup.find("div", {"id": "resultStats"})

	if(results.text == ""):
		print("wtf?")
	else:
		print(results.text)


# ----get the news----

base_url = "https://timesofindia.indiatimes.com"

payload = requests.get(base_url)
payload_code = BeautifulSoup(payload.content, 'html.parser')

news_dump = open("news_dump.txt", 'a')

for titles in payload_code.find_all('a', title=True):
	# print(links['title']) # I got all the news titles

	single_news_title = titles['title']

	news_dump.write(single_news_title + '\n') # append the titles to the txt file

	#google_search_it(single_news_title)

news_dump.close()

links_dump = open('links_dump.txt', 'w')

for links in payload_code.find_all('a', href=True):

	if links.has_attr('href') and links.has_attr('title'):

		complete_title = links['title']

		if links['href'][:4] != 'http':
			complete_link = base_url + links['href']
		
		if len(complete_title.split()) > 3:
			links_dump.write(complete_title + '\n' + complete_link + '\n\n\n')

links_dump.close() 