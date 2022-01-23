import requests
from bs4 import BeautifulSoup

# Defines headers to enable full html access. Websites will often hide html text if headers aren't specified
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

url = "https://www.thebluealliance.com/event/2019casj#event-insights"
#url2 = "https://www.thebluealliance.com/team/2367/2019"
result = requests.get("https://www.thebluealliance.com/team/2367/2019")
result.headers = HEADERS
print(result.status_code)
#print(result.content)
res = requests.get(url, headers=HEADERS) # Scrapes html. Uses headers to receive all html code.
#res2 = requests.get(url2, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser") # Parsing the html text
resSoup = BeautifulSoup(result.text, "html.parser")
links = resSoup.find_all("a")
urlQuals = []
for link in links:
	if "Quals" in link.text:
		print(link)
		print(link.attrs['href'])
		currentURL = "https://www.thebluealliance.com" + link.attrs['href']
		print(currentURL)
		urlQuals.append(currentURL)
for i in range(len(urlQuals)):
	#print(urlQuals[i])
	qUrl = urlQuals[i]
	resQ = requests.get(qUrl, headers=HEADERS)
	soupQ = BeautifulSoup(resQ.text, "html.parser")
	elementsQ = soupQ.find_all("table", {"class" : "match-table"} )
	teamQ = str(elementsQ[0])
	soupQ = BeautifulSoup(teamQ, "html.parser")
	elementsQ = soupQ.find_all("a")
	teamsQ = []
	print(elementsQ[0])
	#for i in elementsQ
print(elementsQ[0])
#soup2 = BeautifulSoup(res2.text, "html.parser")
elements = soup.find_all("table", {"class" : "table table-condensed table-striped table-center"}) # Finds all elements with the given html attribute, and its value. Stores into list.
#elements2 = soup2.find_all("table", {"class" : "table table-condensed table-striped table-center"}) # Finds all elements with the given html attribute, and its value. Stores into list.

''' How the html element will appear in the inspect element menu:
<table class = musicTable> *random text here* </table>
'''
#print(soup)

team = str(elements[1])
#team2 = str(elements2)
soup = BeautifulSoup(team, "html.parser")
#soup2 = BeautifulSoup(team, "html.parser")
elements = soup.find_all("a")
#print(str(team2))
teams = []
opr = []

for i in elements:
    teams.append(i.text) # print each element found

elements = soup.find_all("td")
for i, x in enumerate(elements):
	if i % 2 == 1:
		opr.append(x.text)

for i, x in enumerate(teams):
	print(x + " " + opr[i])

