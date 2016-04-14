## General Hockey Functions

# All Teams
Anaheim = ["Anaheim Ducks", "Anaheim", "ducks", "ANA", "Anh"]
Arizona = ["Arizona Coyotes", "Arizona", "coyotes", "PHX", "AR", "ARZ", "Ari", "ARI"]
Boston = ["Boston Bruins", "Boston", "bruins", "BOS", "Bos"]
Buffalo = ["Buffalo Sabres", "Buffalo", "sabres", "BUF", "Buf"]
Calgary = ["Calgary Flames", "Calgary", "flames", "CGY", "CAL", "Cgy"]
Carolina = ["Carolina Hurricanes", "Carolina", "hurricanes", "CAR", "Car"]
Chicago = ["Chicago Blackhawks", "Chicago", "blackhawks", "CHI", "Chi"]
Colorado = ["Colorado Avalanche", "Colorado", "avalanche",  "COL", "Col"]
Columbus = ["Columbus Blue Jackets", "Columbus", "blue-jackets", "CBJ" "Cls", "CLS"]
Dallas = ["Dallas Stars", "Dallas", "stars", "DAL", "Dal"]
Detroit = ["Detroit Red Wings", "Detroit", "red-wings", "DET", "Det"]
Edmonton = ["Edmonton Oilers", "Edmonton", "oilers", "EDM", "Edm"]
Florida = ["Florida Panthers", "Florida", "panthers", "FLA", "Fla"]
Los_Angeles = ["Los Angeles Kings", "Los Angeles", "kings", "LA", "LAK"]
Minnesota = ["Minnesota Wild", "Minnesota", "wild", "MIN", "Min"]
Montreal = ["Montreal Canadiens", "Montreal", "canadiens", "MTL", "MON", "Mon"]
Nashville = ["Nashville Predators", "Nashville", "predators", "NAS", "NSH", "Nsh"]
New_Jersey = ["New Jersey Devils", "New Jersey", "devils", "NJD", "NJ"]
New_York_I = ["New York Islanders", "NYI", "islanders"]
New_York_R = ["New York Rangers", "NYR", "rangers"]
Ottawa = ["Ottawa Senators", "Ottawa", "senators", "OTT", "Ott"]
Philadelphia = ["Philadelphia Flyers", "Philadelphia", "flyers", "PHI", "Phi"]
Pittsburgh = ["Pittsburgh Penguins", "Pittsburgh", "penguins", "PIT", "Pit"]
San_Jose = ["San Jose Sharks", "San Jose", "sharks", "SJ", "SJS"]
St_Louis = ["St Louis Blues", "St Louis", "blues", "STL", "StL", "Stl"]
Tampa_Bay = ["Tampa Bay Lightning", "Tampa Bay", "lightning", "TB", "TBL", "Tbl"]
Toronto = ["Toronto Maple Leafs", "Toronto", "leafs", "TOR", "TML", "Tor"]
Vancouver = ["Vancouver Canucks", "Vancouver", "canucks", "VAN", "Van"]
Washington = ["Washington Capitals", "Washington", "capitals", "WAS", "WSH", "Was"]
Winnipeg = ["Winnipeg Jets", "Winnipeg", "jets", "WIN", "WPG", "Wpg"]






# Checks if the two teams are the same
# str, str -> Bool
def team_equal(team1, team2):
    if team1 in Anaheim and team2 in Anaheim:
        return True
    if team1 in Arizona and team2 in Arizona:
        return True
    if team1 in Boston and team2 in Boston:
        return True
    if team1 in Buffalo and team2 in Buffalo:
        return True
    if team1 in Calgary and team2 in Calgary:
        return True
    if team1 in Carolina and team2 in Carolina:
        return True
    if team1 in Chicago and team2 in Chicago:
        return True
    if team1 in Colorado and team2 in Colorado:
        return True
    if team1 in Columbus and team2 in Columbus:
        return True
    if team1 in Dallas and team2 in Dallas:
        return True
    if team1 in Detroit and team2 in Detroit:
        return True
    if team1 in Edmonton and team2 in Edmonton:
        return True
    if team1 in Florida and team2 in Florida:
        return True
    if team1 in Los_Angeles and team2 in Los_Angeles:
        return True
    if team1 in Minnesota and team2 in Minnesota:
        return True
    if team1 in Montreal and team2 in Montreal:
        return True
    if team1 in Nashville and team2 in Nashville:
        return True
    if team1 in New_Jersey and team2 in New_Jersey:
        return True
    if team1 in New_York_I and team2 in New_York_I:
        return True
    if team1 in New_York_R and team2 in New_York_R:
        return True
    if team1 in Philadelphia and team2 in Philadelphia:
        return True
    if team1 in Pittsburgh and team2 in Pittsburgh:
        return True
    if team1 in Ottawa and team2 in Ottawa:
        return True
    if team1 in San_Jose and team2 in San_Jose:
        return True
    if team1 in St_Louis and team2 in St_Louis:
        return True
    if team1 in Tampa_Bay and team2 in Tampa_Bay:
        return True
    if team1 in Toronto and team2 in Toronto:
        return True
    if team1 in Vancouver and team2 in Vancouver:
        return True
    if team1 in Washington and team2 in Washington:
        return True
    if team1 in Winnipeg and team2 in Winnipeg:
        return True
    else: return False


