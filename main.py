from chessdotcom import *
import pprint
import requests

# printer = pprint.PrettyPrinter()

def get_player_rating(username):
    data = get_player_stats(username).json
   
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
    print(data)
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
    
    date = games['games'][-1]['pgn'].splitlines()[2] #date
    # print(games['games'][-1]['pgn'].splitlines()) 
    player_1 =(games['games'][-1]['pgn'].splitlines()[4]) #white-player
    player_2 =(games['games'][-1]['pgn'].splitlines()[5]) #black-plater
    result = (games['games'][-1]['pgn'].splitlines()[6]) #result
    ouverture = (games['games'][-1]['pgn'].splitlines()[10]) #ouverture je crois
    white_elo = (games['games'][-1]['pgn'].splitlines()[13]) #white-elo
    black_elo = (games['games'][-1]['pgn'].splitlines()[14]) #black elo
    duration_game = (games['games'][-1]['pgn'].splitlines()[15]) #time_game
    result_precis = (games['games'][-1]['pgn'].splitlines()[16]) #result_better

    start_game = (games['games'][-1]['pgn'].splitlines()[17]) #debut de la partie
    end_game  = (games['games'][-1]['pgn'].splitlines()[19]) #fin

    total_game = "0"
    print("la derniere partie de ", username ,"entre", player_1, white_elo ,"et", player_2, black_elo, "a eu lieu ce ", date, 
    "et a commence par une", ouverture, ". La partie a commencé a:", start_game, "et a fini a ", end_game, "\nLe resultat de celle-ci:", result_precis)

   
    #print(games['games'][-1]["pgn"])


    # for game in games['games']:
    #     game_url = game['url']
    # print(game_url)
    # printer.pprint(game)

#get_player_rating('timruscica')
get_most_recent_game('pgmendormi')
