def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    return
    game_choice = input("Enter the number of the game you want to play: ")
    difficulty = input("Please choose game difficulty from 1 to 5: ")

    # Validate game choice and difficulty input
    if game_choice not in ['1', '2', '3']:
        print("Invalid game choice. Please try again.")
        return

    if difficulty not in ['1', '2', '3', '4', '5']:
        print("Invalid difficulty level. Please try again.")
        return

    # Game logic goes here
    # You can implement the different games based on the user's input

