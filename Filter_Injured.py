## Filter Out Injured

import requests
from bs4 import BeautifulSoup

# Creates a list of injured players
# None -> listof(Players)
def injured_players():
    injuries_page = requests.get("http://www.rotoworld.com/teams/injuries/nhl/all/")
    injuries_page = BeautifulSoup(injuries_page.content, "html.parser")

    injured_players = []

    for line in injuries_page.find_all("td"):
        if "/player/nhl/" in str(line):
            name = str(line).split(">")[2]
            name = name.split("<")[0]
            injured_players.append(name)
    return injured_players




# Filters Injured Players Out of LOP
# listof(Players) -> listof(Players)
def filter_out_injured(lop):
    inj_players = injured_players()

    healthy_players = []

    for player in lop:
        name = player[0]
        if name not in inj_players:
            healthy_players.append(player)
        else:
            pass
    return healthy_players

