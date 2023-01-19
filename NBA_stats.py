"""
Working with NBA statistics and working with them in Python. Trying to learn more about working with JSON. Also got to
use PrettyPrinter for JSON.

Heavily based on code from: youtube.com/watch?v=txKBWtvV99Y
"""
from requests import get
from pprint import PrettyPrinter

# URL things
BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

# Pretty printer to print JSON nicely
printer = PrettyPrinter()


# Get a list of all the links
def get_links():
    return get(BASE_URL + ALL_JSON).json()['links']


# Get the games of the current day
def get_scoreboard():
    # Games data
    games = get(BASE_URL + get_links()['currentScoreboard']).json()['games']

    # Nice formatted print with teams, score, and time
    for game in games:
        print("------------------------------------------")
        print(f"{game['hTeam']['triCode']} vs {game['vTeam']['triCode']}")
        print(f"{game['hTeam']['score']} - {game['vTeam']['score']}")
        print(f"{game['clock']} - {game['period']['current']}")


# Get the statistics of the teams
def get_stats():
    # Get stat leaders
    stats = get_links()['leagueTeamStatsLeaders']
    # Get teams
    teams = get(
        BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    # Cleaning and sorting teams
    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    # Printing everything out nicely
    for i, team in enumerate(teams):
        print(f"{i + 1}. {team['name']} - {team['nickname']} - {team['ppg']['avg']}")


get_scoreboard()
get_stats()
