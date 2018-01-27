import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def check_if_legit(domain_name):

	global true_points

	if domain_name in legit_sites:
		true_points += 1

def get_the_domain_name(complete_link):

	broken_url = urlparse(complete_link)
	domain_name = '{uri.scheme}://{uri.netloc}/'.format(uri=broken_url)

	if(domain_name[:5] == 'https'):
		domain_name = domain_name.replace('https://www.', '')
		domain_name = domain_name.replace('https://', '')

		if(domain_name[-1] == '/'):
			domain_name = domain_name[:-1]

		check_if_legit(domain_name)
		domains_list.append(domain_name)
		return

	if(domain_name[:4] == 'http'):
		domain_name = domain_name.replace('http://www.', '')
		domain_name = domain_name.replace('https://', '')

		if(domain_name[-1] == '/'):
			domain_name = domain_name[:-1]

		check_if_legit(domain_name)
		domains_list.append(domain_name)

def google_search_it(query):
	r = requests.get("https://www.google.com/search", params={'as_epq':query, 'num':100}) # advanced search

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
				#print(complete_title + '\n' + complete_link + '\n\n\n')

			get_the_domain_name(complete_link)

domains_list = []

true_points = 0

with open("dataset.txt") as data_file:
    legit_sites = data_file.readlines()

legit_sites = [x.strip() for x in legit_sites]

query = "modi"
google_search_it(query)

print(true_points)
#print(domains_list)