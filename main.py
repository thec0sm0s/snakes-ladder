import random


SNAKES_POS = {17: 7, 54: 34, 62: 19, 98: 79}
LADDERS_POS = {3: 38, 24: 33, 42: 93, 72: 84}


def get_player_name(player):
    return input(f"Enter name of {player}: ")


def handle_game_turn(player):
    throw = input(f"[{player['name']}] Enter roll for auto mode or any number from 1-20: ")
    if throw.upper() == "QUIT":
        return "QUIT"
    elif throw.upper() == "ROLL":
        outcome = random.randint(1, 6)
        print(f"Your dice outcome is {outcome}.")
    elif int(throw) > 0 and int(throw) <= 20:
        outcome = int(throw)
    else:
        print(f"Invalid throw input. {player['name']} please try again.")
        return handle_game_turn(player)

    future_position = player["position"] + outcome
    
    if future_position > 100:
        print(f"{player['name']} keep trying!")
        return "TRY_AGAIN_NEXT_TURN"
    
    player["position"] = future_position

    if player["position"] == 100:
        return "WON"
    
    if player["position"] in SNAKES_POS:
        player["position"] = SNAKES_POS[player["position"]]
        print("~~~~~~~~Snake Bite~~~~~~~~")
        print(f"{player['name']}, you went down to position {player['position']}.")
    elif player["position"] in LADDERS_POS:
        player["position"] = LADDERS_POS[player["position"]]
        print("# # # # # Ladder # # # # #")
        print(f"{player['name']}, you went up to position {player['position']}.")

    print(f"{player['name']}, your current position is {player['position']}.")

    return "NEXT_TURN"
    


def get_current_player(players, turn):
    if turn % 2 == 0:
        return players[1]
    return players[0]


def main(players):
    winner = None
    turn = 1
    while True:
        current_player = get_current_player(players, turn)
        rv = handle_game_turn(current_player)
        if rv == "QUIT":
            winner = get_current_player(players, turn + 1)
            break
        elif rv == "WON":
            winner = current_player
            break
        turn += 1
    print(f"Congratualtions {winner['name']} for winning the game.")


if __name__ == "__main__":
    player1 = {"name": get_player_name('Player 1'), "position": 0}
    player2 = {"name": get_player_name('Player 2'), "position": 0}

    players = (player1, player2)
    
    main(players)
