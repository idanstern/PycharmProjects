import random
import time
from Live import load_game

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []
        self.user_list = []

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        self.user_list = []
        for i in range(self.difficulty):
            while True:
                try:
                    num = int(input(f"Enter number {i + 1}: "))
                    if 1 <= num <= 101:
                        self.user_list.append(num)
                        break
                    else:
                        print("Please enter a number between 1 and 101.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def is_list_equal(self):
        return self.sequence == self.user_list

    def play(self):
        self.generate_sequence()
        print("Memorize the following numbers:")
        print(self.sequence)
        time.sleep(0.7)
        print("\n" * 100)  # Clear the screen
        print("Now, enter the numbers you remember:")
        self.get_list_from_user()
        return self.is_list_equal()

# Example usage
if __name__ == "__main__":
    difficulty_level = game_difficulty
    game = MemoryGame(difficulty_level)
    game_result = game.play()
    if game_result:
        print("Congratulations! You remembered all the numbers correctly!")
    else:
        print("Sorry, you got some or all of the numbers wrong. You lost!")
