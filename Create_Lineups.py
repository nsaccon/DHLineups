## This file gathers all the information

from Run_Daily import all_skaters, all_goalies


all_centers = list(filter((lambda x : x[1] == "C"), all_skaters))
all_wingers = list(filter((lambda x : x[1] == "LW" or x[1] == "RW"), all_skaters))
all_defenceman = list(filter((lambda x : x[1] == "D"), all_skaters))



