import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def score_generator():

	score = true_points - (false_points * 3)

	if(false_points >= 3):
		score -= false_points * false_points
	if(true_points <= 5):
		score /= 4
	elif(true_points <= 8):
		score /= 3
	elif(true_points <= 10):
		score /= 2
	elif(true_points <= 13):
		score /= 1.5

	if(true_points == 0 and false_points == 0):
		score=-1
		return score

	score = score / (true_points + false_points)

	if(score < 0):
		score = 0
	elif(score >= 1):
		score = 0.9

	print("Truth probability = " + str("{:.3f}".format(score)))
	#return  str("{:.3f}".format(score))
	return "{:.3f}".format(score)

def check_if_legit(domain_name):

	global true_points
	global false_points

	if domain_name in legit_sites:
		true_points += 1

	if domain_name in illegit_sites:
		false_points += 1

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
	r = requests.get("https://www.google.com/search", params={'q':query, 'num':100}) # advanced search 'as_epq'

	soup = BeautifulSoup(r.text, "lxml")
	results = soup.find("div", {"id": "resultStats"})

	'''if(results.text == ""):
		print("wtf?")
	else:
		print(results.text)'''

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

def start_predict(query):

	global true_points, false_points
	global legit_sites, illegit_sites

	with open("fakenewsFE\\true_dataset.txt") as true_data:
	    legit_sites = true_data.readlines()
	legit_sites = [x.strip() for x in legit_sites]

	with open("fakenewsFE\\fake_dataset.txt") as fake_data:
	    illegit_sites = fake_data.readlines()
	illegit_sites = [x.strip() for x in illegit_sites]

	fake_words = ['fake', 'hoax', 'lie', 'lies', 'lies', 'false', 'illegitimate', 'rumour', 'counterfeit', 'forged', 'fictitious', 'fabricated', 'fraud']

	query_list = query.split()

	for i in query_list:
		if i in fake_words:
			false_points += 1

	google_search_it(query)

	score=score_generator()
	return score

	#print('True score: ' + str(true_points))
	#print('False score: ' + str(false_points))


domains_list = []

true_points = 0
false_points = 0

legit_sites = []
illegit_sites = []

#start_predict("modi prime minister")
