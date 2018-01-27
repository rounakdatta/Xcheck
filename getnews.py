import requests
from bs4 import BeautifulSoup
import argparse

# ----google search it---  ## remember to refresh your IP everytime you robot-search google

def google_search_it(query):
	r = requests.get("https://www.google.com/search", params={'q':query})

	soup = BeautifulSoup(r.text, "lxml")
	results = soup.find("div", {"id": "resultStats"})

	if(results.text == ""):
		print("wtf?")
	else:
		print(results.text)


# ----get the news----

base_url = "https://in.reuters.com"

payload = requests.get(base_url)
payload_code = BeautifulSoup(payload.content, 'html.parser')

'''news_dump = open("news_dump.txt", 'a')

for titles in payload_code.find_all('a', title=True):
	# print(links['title']) # I got all the news titles

	single_news_title = titles['title']

	news_dump.write(single_news_title + '\n') # append the titles to the txt file

	google_search_it(single_news_title)

news_dump.close()'''

links_dump = open('links_dump.txt', 'w')                                                # scrape sites like TOI, ET

for links in payload_code.find_all('a', href=True):

	if links.has_attr('href') and links.has_attr('title'):

		complete_title = links['title']

		if links['href'][:4] != 'http':
			complete_link = base_url + links['href']
		
		if len(complete_title.split()) > 3:
			links_dump.write(complete_title + '\n' + complete_link + '\n\n\n')

for links_a in payload_code.find_all('a'):                                              # scrape sites which have content within <a>

	if links_a.has_attr('href'):

		complete_title = ''.join(links_a.findAll(text=True))

		complete_link = links_a['href']

		if links_a['href'][:4] != 'http':
			complete_link = base_url + links_a['href']

		if len(complete_title.split()) > 3:
			links_dump.write(complete_title + '\n' + complete_link + '\n\n\n')

for links_p in payload_code.find_all('p'):                                              # scrape sites which have content within <p>

	if links_p.has_attr('href'):

		complete_title = ''.join(links_p.findAll(text=True))

		complete_link = links_p['href']

		if links_p['href'][:4] != 'http':
			complete_link = base_url + links_p['href']
		
		if len(complete_title.split()) > 3:
			links_dump.write(complete_title + '\n' + complete_link + '\n\n\n')


links_dump.close() 