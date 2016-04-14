## Run daily to write files with all the players with adjusted daily values.

from Create_Players_From_CSV import skaters_lst
from Create_Players_From_CSV import goalies_lst
from Create_Players import grab_averages
from Goalies_With_Odds import goalie_grab_averages
from Filter_Injured import filter_out_injured


def create_daily_files():
    all_skaters = grab_averages(skaters_lst)
    all_goalies = goalie_grab_averages(goalies_lst)

    # Filter Out Injured Players
    all_skaters = filter_out_injured(all_skaters)

    # Write Skater File:
    daily_skater = open('Daily_Skater.txt', 'w')
    daily_skater.write(str(all_skaters))
    daily_skater.close()

    # Write Goalie File:
    daily_goalie = open('Daily_Goalie.txt', 'w')
    daily_goalie.write(str(all_goalies))
    daily_goalie.close()



# Read Skater File
all_skaters = open("Daily_Skater.txt", "r")
all_skaters = all_skaters.read()
all_skaters = eval(all_skaters)

# Read Goalie File
all_goalies = open("Daily_Goalie.txt", "r")
all_goalies = all_goalies.read()
all_goalies = eval(all_goalies)