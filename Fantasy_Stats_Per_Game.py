## Player's Fantasy Stats This Season

import requests
from bs4 import BeautifulSoup

# Chnages a players

def name_fix(player):
    name = player[0]
    if name == "Alex Ovechkin":
        return "Alexander Ovechkin"
    if name == "Kris Letang":
        return "kristopher Letang"
    if name == "Michael Cammalleri":
        return "Mike Cammalleri"
    if name == "Pierre-Alexandre Parenteau":
        return "Pierre Parenteau"
    if name == "Niklas Kronwall":
        return "Niklas Kronvall"
    if name == "Dmitry Kulikov":
        return "Dmitri Kulikov"
    if name == "Dan Girardi":
        return "Daniel Girardi"
    if name == "Johnny Oduya":
        return "David Johnny Oduya"
    if name == "Toby Enstrom":
        return "Tobias Enstrom"
    if name == "Andy Greene":
        return "Andrew Greene"
    if name == "Alex Burmistrov":
        return "Alexander Burmistrov"
    if name == "Chris Higgins":
        return "Christopher Higgins"
    if name == "Matt Calvert":
        return "Matthew Calvert"
    if name == "Matt Nieto":
        return "Matthew Nieto"
    if name == "Chris Neil":
        return "Christopher Neil"
    if name == "Rob Scuderi":
        return "Robert Scuderi"
    if name == "Matt Stajan":
        return "Matthew Stajan"
    if name == "Drew Miller":
        return "Andrew Miller"
    if name == "Mike Blunden":
        return "Michael Blunden"
    if name == "Tom Sestito":
        return "Tommy Sestito"
    if name == "Mike Santorelli":
        return "Michael Santorelli"
    if name == "T.J. Brennan":
        return "TJ Brennan"
    if name == "J.C. Lipon":
        return "JC Lipon"
    else:
        return name







# Creates a list of yo to 82 Games the player has played in form [Name, Arena, Fantast_Points]
# Player -> listof(Games)
def player_fantasy_stats_by_game(player):
    games = []

    name = name_fix(player)
    name_url = name.replace(" ", "-")
    player_page = requests.get("http://dobberhockey.com/players/"+name_url)
    player_page = BeautifulSoup(player_page.content, "html.parser")

    for line in player_page.find_all("tr"):
        # Game is in form [Name, Arena, Fantast_Points]
        if "did-play" in str(line):

            # Goals
            goals = str(line).split(" ")[19]
            goals = goals.split(">")[1]
            goals= int(goals.split("<")[0])

            # Assists
            assists = str(line).split(" ")[23]
            assists = assists.split(">")[1]
            assists= int(assists.split("<")[0])

            # Shots
            shots = str(line).split(" ")[39]
            shots = shots.split(">")[1]
            shots= int(shots.split("<")[0])

            # Blocks
            blocks = str(line).split(" ")[55]
            blocks = blocks.split(">")[1]
            blocks= int(blocks.split("<")[0])

            # Arena
            arena = "Home"
            if "@" in str(line).split(" ")[15]:
                arena = "Away"

            # Fantasy points from goals
            goal_points = goals*3
            if goals >= 3:
                goal_points += 2

            # Collect Info
            fantasy_points = goal_points + assists*2 + shots*0.5 + blocks*0.5
            game = [player[0], arena, fantasy_points]
            games.append(game)

    return games


# Creates Averages in form [Name, Last10, Home, Away]

def player_averages(player):

    games = player_fantasy_stats_by_game(player)

    # Last 10
    last10 = games[:9]
    l10_Fpoints = 0
    for game in last10:
        l10_Fpoints += game[2]

    if len(last10) == 0:
        l10_average = 0
    else:
        l10_average = round(l10_Fpoints / len(last10), 3)

    # Home
    h_games = list(filter((lambda x : x[1] == "Home"), games))
    h_points = 0
    for game in h_games:
        h_points += game[2]

    if len(h_games) == 0:
        h_average = 0
    else:
        h_average = round(h_points / len(h_games), 3)

    # Away
    a_games = list(filter((lambda x : x[1] == "Away"), games))
    a_points = 0
    for game in a_games:
        a_points += game[2]

    if len(a_games) == 0:
        a_average = 0
    else:
        a_average = round(a_points / len(a_games), 3)


    return [player[0], l10_average, h_average, a_average]


#print(player_averages(['Connor McDavid', 'C', 7300, 'Edm', 'Home', 'Van', 7, 3.721]))