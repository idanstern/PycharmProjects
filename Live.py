# welcome(name)
def welcome(name):
    return f"\nHello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"

# load game()
def load_game():
    game_choice = 0
    game_difficulty = 0
    while int(game_choice) > 3 or int(game_choice) < 1:
        game_choice = input("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                            "2. Guess Game - guess a number and see if you chose like the computer\n"
                            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n\n"
                            "please choose a game to play: ")
        while not game_choice.isnumeric():
            game_choice = input("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                            "2. Guess Game - guess a number and see if you chose like the computer\n"
                            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n\n"
                            "please choose a game to play: ")
    game_list = ["Memory game", "Guess game", "Currency Roulette"]
    print(f"Welcome to {game_list[(int(game_choice)-1)]}")

# difficulty
    while int(game_difficulty) > 5 or int(game_difficulty) < 1:
        game_difficulty = input("Please choose game difficulty from 1 to 5: ")
        while not game_difficulty.isnumeric():
            game_difficulty = input("Please choose game difficulty from 1 to 5: ")
    return game_choice, game_difficulty