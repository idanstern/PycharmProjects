from Live import load_game, welcome
from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
name = input("please enter your name: ")
print(welcome(name))
game, difficulty = load_game()
if game == 1:
    game = MemoryGame(difficulty)
    MemoryGame.play()
if game == 2:
    game = GuessGame(difficulty)
    GuessGame.play()
if game == 3:
    game = CurrencyRouletteGame(difficulty)
    CurrencyRouletteGame.play()