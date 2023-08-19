import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self):
        # Fetch the current exchange rate from USD to ILS using a free currency API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        exchange_data = response.json()
        usd_to_ils_rate = exchange_data["rates"]["ILS"]

        # Generate the money interval based on the difficulty level
        total_value_of_money = random.randint(1, 100)
        lower_bound = total_value_of_money - (5 - self.difficulty)
        upper_bound = total_value_of_money + (5 - self.difficulty)

        # Convert the bounds to ILS
        lower_bound_ils = round(lower_bound * usd_to_ils_rate, 2)
        upper_bound_ils = round(upper_bound * usd_to_ils_rate, 2)

        return lower_bound_ils, upper_bound_ils

    def get_guess_from_user(self):
        while True:
            try:
                user_guess = float(input("Enter your guess for the value in ILS: "))
                return user_guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        lower_bound_ils, upper_bound_ils = self.get_money_interval()
        user_guess = self.get_guess_from_user()

        print(f"The correct value is between {lower_bound_ils} ILS and {upper_bound_ils} ILS.")
        print("Your guess:", user_guess)

        if lower_bound_ils <= user_guess <= upper_bound_ils:
            print("Congratulations! You guessed correctly!")
            return True
        else:
            print("Sorry, you guessed wrong!")
            return False

# Example usage:
if __name__ == "__main__":
    difficulty_level = 3  # You can set any difficulty level you want
    currency_game = CurrencyRouletteGame(difficulty_level)
    currency_game.play()
