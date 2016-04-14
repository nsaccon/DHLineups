## NHL DraftKings Optimizer

import csv

readDKSalaries = open("DKSalaries.csv") # Testing File
#readDKSalaries = open("DKSalaries.csv")
readDKSalaries = csv.reader(readDKSalaries, delimiter=",")



# Takes a string in the form 'Team1@Team2 XX:XXPM ET' and gets the opposing team
# Str, Str -> Str
def info_to_opponent(info_str, plr_team):
   teams = info_str.split(" ")[0]
   teams = teams.split("@")
   for opponent in teams:
      if opponent != plr_team:
         return opponent

# Takes a string in the form 'Team1@Team2 XX:XXPM ET' and gets the start time
# Str, Str -> Str
def info_to_start_time(info_str):
   time = info_str.split(" ")[1]
   time = time.split(":")
   return int(time[0])

# Takes a string in the form 'Team1@Team2 XX:XXPM ET' and gets Home or Away
# Str, Str -> Str
def info_to_arena(info_str, plr_team):
   arena = info_str.split(" ")[0]
   arena = arena.split("@")
   if arena[0] == plr_team:
      return "Away"
   else: return "Home"



# Creates players in form [ Name, Position, Salary, Team, Arena, Opponent, Start Time, Average Points ]
# readDKSalaries -> Listof(Players)

def csv_create_players(csv_doc):
   todays_players = []
   for line in csv_doc:
      if line[0] != 'Position':
         name = line[1]
         position = line[0]
         salary = int(line[2])
         average_points = float(line[4])
         team = line[5]
         opponent = info_to_opponent(line[3],team)
         start_time = info_to_start_time(line[3])
         arena = info_to_arena(line[3], team)
         todays_players.append([name, position, salary, team, arena, opponent, start_time, average_points])
   return todays_players

# Players & Goalies
players_lst = csv_create_players(readDKSalaries)
#Players
skaters_lst = list(filter((lambda x : x[1] != "G"), players_lst))
#Goalies
goalies_lst = list(filter((lambda x : x[1] == "G"), players_lst))
