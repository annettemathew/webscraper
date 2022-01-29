import requests
from bs4 import BeautifulSoup

# Defines headers to enable full html access. Websites will often hide html text if headers aren't specified
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

url = "https://open.spotify.com/playlist/1ZhPAjegWrOsnhsAqOWnvu?si=db6c2154178c424e"

res = requests.get("https://www.thebluealliance.com/team/2367/2019", headers=HEADERS) # Scrapes html. Uses headers to receive all html code.
soup = BeautifulSoup(res.text, "html.parser") # Parsing the html text
table = soup.find_all("table", {"class": "match-table"})

soup = BeautifulSoup(str(table[1]), "html.parser")
teams = soup.find_all("td", {"colspan":"2"})
numbers = []

for i in teams:
    soup = BeautifulSoup(str(i), "html.parser")
    numbers.append(soup.find_all("a"))

red_alliance = []
blue_alliance = []
x = 1
for i in numbers:
    try:
        if x < 4:
            red_alliance.append(i[0].text)
        else:
            blue_alliance.append(i[0].text)

        if x < 6:
            x += 1
        else:
            x = 0
    except:
        continue

for i in red_alliance:
    print(i)