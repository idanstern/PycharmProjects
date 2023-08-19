import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                user_guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= user_guess <= self.difficulty:
                    return user_guess
                else:
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, user_guess):
        return user_guess == self.secret_number

    def play(self):
        self.generate_number()
        user_guess = self.get_guess_from_user()

        print("Secret Number:", self.secret_number)
        print("Your Guess:", user_guess)

        if self.compare_results(user_guess):
            print("Congratulations! You guessed correctly!")
            return True
        else:
            print("Sorry, you guessed wrong!")
            return False


# Example usage:
if __name__ == "__main__":
    difficulty_level = 10  # You can set any difficulty level you want
    guess_game = GuessGame(difficulty_level)
    guess_game.play()
