from chessdotcom import *
import requests



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
        
def parser(var):
    test = []
    j = 0
    for i in var:
        if (i.isnumeric()):
            test.append(i)
            j+=1

    try:
        result = str(test[0]) + str(test[1])
    except Exception:
        result = str(test[0])
    return(result)

def get_most_recent_game(username):
    data = get_player_game_archives(username).json


    url = data['archives'][-1]
    games = requests.get(url).json()
    
    game = games['games'][-1]
    print(games['games'][-1]['url'])
    
    date = games['games'][-1]['pgn'].splitlines()[2] #date
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


    start_game =start_game.split(':')
    end_game = end_game.split(':')

    start_game[0] = parser(start_game[0])
    start_game[2] = parser(start_game[2])
    end_game[0] = parser(end_game[0])
    end_game[2] = parser(end_game[2])

    start_game2 = int(int(start_game[0]) * 3600 + int(start_game[1]) * 60 + int(start_game[2]) * 1)

    end_game2 = int(end_game[0]) * 3600 + int(end_game[1]) * 60 + int(end_game[2])

    total_game = end_game2 - start_game2

    hours = str(total_game // 3600)
    minutes = str(total_game // 60)  # Truncating integer division
    secondes = str(total_game % 60)

    dureepartie = (hours + " heures " + minutes+ " minutes "+ secondes + " secondes")
    print("la derniere partie de ", username ,"entre", player_1, white_elo ,"et", player_2, black_elo, "a eu lieu ce ", date, 
    "et a commence par une", ouverture, ". La partie a commencé a:", start_game,"a duré", dureepartie , "et a fini a ", end_game, "\nLe resultat de celle-ci:", result_precis)



#get_player_rating('timruscica')
get_most_recent_game('pgmendormi')
