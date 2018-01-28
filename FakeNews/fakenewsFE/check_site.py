from urllib.parse import urlparse

def check_if_legit(domain_name):

	true_points = 0

	if domain_name in illegit_sites:
		return "Fake / Malicious"

	if domain_name in legit_sites:
		return ("Authentic")

	return "Not found as a news aggregator"

def checker(complete_link):

	global legit_sites
	global illegit_sites

	with open("fakenewsFE\\true_dataset.txt") as true_data:
		legit_sites = true_data.readlines()
	legit_sites = [x.strip() for x in legit_sites]

	with open("fakenewsFE\\fake_dataset.txt") as fake_data:
		illegit_sites = fake_data.readlines()
	illegit_sites = [x.strip() for x in illegit_sites]

	broken_url = urlparse(complete_link)

	domain_name = '{uri.scheme}://{uri.netloc}/'.format(uri=broken_url)

	if(domain_name[:4] != 'http'):
		domain_name = "http://" + domain_name

	print(domain_name)

	if(domain_name[:5] == 'https'):
		domain_name = domain_name.replace('https://www.', '')
		domain_name = domain_name.replace('https://', '')

		if(domain_name[-1] == '/'):
			domain_name = domain_name[:-1]

		outputx = check_if_legit(domain_name)
		return outputx

	if(domain_name[:4] == 'http'):
		domain_name = domain_name.replace('http://www.', '')
		domain_name = domain_name.replace('https://', '')

		if(domain_name[-1] == '/'):
			domain_name = domain_name[:-1]

		outputx = check_if_legit(domain_name)
		return outputx

	domain_name = domain_name.replace('www.', '')

	if(domain_name[-1] == '/'):
		domain_name = domain_name[:-1]

	outputx = check_if_legit(domain_name)
	return outputx

legit_sites = []
illegit_sites = []

pp = checker("http://www.ndtv.com")

#print(legit_sites)
print(pp)
