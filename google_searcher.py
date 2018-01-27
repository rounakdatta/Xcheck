import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_the_domain_name(complete_link):

	broken_url = urlparse(complete_link)
	domain_name = '{uri.scheme}://{uri.netloc}/'.format(uri=broken_url)

	if(domain_name[:4] == 'http'):
		print(domain_name)

def google_search_it(query):
	r = requests.get("https://www.google.com/search", params={'as_epq':query}) # advanced search

	soup = BeautifulSoup(r.text, "lxml")
	results = soup.find("div", {"id": "resultStats"})

	if(results.text == ""):
		print("wtf?")
	else:
		print(results.text)

	stories = ''

	for links_a in soup.find_all('a'):

		if links_a.has_attr('href'):

			complete_title = ''.join(links_a.findAll(text=True))

			complete_link = links_a['href']

			if links_a['href'][:4] != 'http':
				complete_link = links_a['href'][7:]

			#if len(complete_title.split()) > 3:
				print(complete_title + '\n' + complete_link + '\n\n\n')

			get_the_domain_name(complete_link)

query = "rahul gandhi is dead"
google_search_it(query)