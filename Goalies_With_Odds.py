## Goalies With Vegas Odds

import requests
from bs4 import BeautifulSoup
from Create_Players_From_CSV import goalies_lst
from General_Functions import team_equal

odds_page = requests.get("http://www.vegasinsider.com/nhl/odds/las-vegas/")
odds_page = BeautifulSoup(odds_page.content, "html.parser")


print(goalies_lst)

# Takes the odds and creates a number to add to the total
# Int -> Float
def odds_to_num(odds):
    if odds >= 100:
        return -(odds/100)
    if odds < 100:
        return -(odds/100)




# Creates a list in the form ["Name", "Odds", "Over/Under"]
# goalie -> listof(str)
def goalie_odds(goalie):
    stopper = 0

    for line in odds_page.find_all("a"):
        if "line-movement" in str(line):

            teams = str(line).split("/")[5]
            team1 = teams.split("-@-")[0]
            team2 = teams.split("-@-")[1].split(".")[0]

            odds = str(line).split()[6].split("<br>")
            odds1 = odds[1]
            odds2 = odds[2]

            if team_equal(team1, goalie[3]):
                stopper += 1
                if stopper == 2:
                    return [goalie[0], int(odds1), odds[0][1]]

            if team_equal(team2, goalie[3]):
                stopper += 1
                if stopper == 2:
                    return [goalie[0], int(odds2), odds[0][1]]



def goalie_grab_averages(log):

    complete_goalie_lst = []

    for goalie in log:
        odds = goalie_odds(goalie)

        if odds[2] == "u":
            goalie[7] += 1
        if odds[2] == "o":
            goalie[7] -= 1

        goalie[7] += odds_to_num(odds[1])
        goalie[7] = round(goalie[7], 3)

        complete_goalie_lst.append(goalie)

    return complete_goalie_lst
