from chessdotcom import *
import pprint
import requests

# printer = pprint.PrettyPrinter()

def get_player_rating(username):
    data = get_player_stats(username).json
   
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
    for category in categories:
        print("---------------------")
        print('Category:', category)
        print(f'Current: {data[category]["last"]["rating"]}')
        print(f'Best: {data[category]["best"]["rating"]}')
        print(f'Best: {data[category]["record"]}')

def get_most_recent_game(username):
    data = get_player_game_archives(username).json


    url = data['archives'][-1]
    games = requests.get(url).json()

    game = games['games'][-1]
    print(games['games'][-1]['url'])

    # for game in games['games']:
    #     game_url = game['url']
    # print(game_url)
    # printer.pprint(game)

# get_player_rating('timruscica')
get_most_recent_game('pgmendormi')
