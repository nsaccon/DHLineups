##  Daily Value Players

from Run_Daily import all_skaters, all_goalies

all_centers = list(filter((lambda x : x[1] == "C"), all_skaters))
all_wingers = list(filter((lambda x : x[1] == "LW" or x[1] == "RW"), all_skaters))
all_defenceman = list(filter((lambda x : x[1] == "D"), all_skaters))


# Takes a player and returns a value
# Player -> Float
def player_value(player):
    cost = player[2]/1000
    points = player[7]
    return round(points/cost, 3)


value_centers = sorted(all_centers, key = lambda x : player_value(x))[::-1]
value_wingers = sorted(all_wingers, key = lambda x : player_value(x))[::-1]
value_defenceman = sorted(all_defenceman, key = lambda x : player_value(x))[::-1]
value_goalies = sorted(all_goalies, key = lambda x : player_value(x))[::-1]


def write_doc_str(lop):
    doc_str = ""
    for player in lop:
        name = player[0]
        cost = player[2]
        value = str(player_value(player))
        line = name + ": " + value + "\n"
        if cost >= 3000:
            doc_str += line
        else:
            pass
    return doc_str


def daily_value_players():
    daily_skater = open('Daily_Value_Players.txt', 'w')
    daily_skater.write("Value Goalies\n\n" + write_doc_str(value_goalies[:10])
                       +"\nValue Centers\n\n" + write_doc_str(value_centers[:10])
                       +"\nValue Wingers\n\n" + write_doc_str(value_wingers[:10])
                       +"\nValue Defenceman\n\n" + write_doc_str(value_defenceman[:10]))
    daily_skater.close()







