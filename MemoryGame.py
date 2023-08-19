import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        print(f"Remember the numbers for 0.7 seconds and then enter the {self.difficulty} numbers:")
        time.sleep(0.7)
        user_input = input("Enter the numbers separated by spaces: ")
        user_list = [int(num) for num in user_input.split()]
        return user_list

    @staticmethod
    def is_list_equal(list1, list2):
        return list1 == list2

    def play(self):
        generated_sequence = self.generate_sequence()
        user_sequence = self.get_list_from_user()

        print("Generated Sequence:", generated_sequence)
        print("Your Sequence:", user_sequence)

        if self.is_list_equal(generated_sequence, user_sequence):
            print("Congratulations! You won!")
            return True
        else:
            print("Sorry, you lost!")
            return False

# Example usage:
if __name__ == "__main__":
    difficulty_level = 5  # You can set any difficulty level you want
    memory_game = MemoryGame(difficulty_level)
    memory_game.play()
