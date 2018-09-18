#jugadores del madrid y sus posiciones
from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.realmadrid.com/futbol/plantilla")
soup = BeautifulSoup(r.text, "html.parser")
listOfNames = []
listOfPositions = []
results = soup.find("div", {"class":"section wide"})
names = results.findAll("span",{"itemprop":"name"})
positions = results.findAll("span",{"itemprop":"jobTitle"})
for item in names:
    players_name = item.find("strong").text
    listOfNames.append(players_name)
for items in positions:
    players_positions = items.text
    listOfPositions.append(players_positions)
for i in range (len(listOfNames)):
    print(listOfNames[i], "       ", listOfPositions[i])
