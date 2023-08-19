# Ask the player to enter a character
player_input = input("Enter a character: ")

# Validate the input
if len(player_input) != 1:
    print("Invalid input! Please enter exactly one character.")
else:
    # Insert the character into a variable
    chosen_character = player_input

    # Print the character to the screen
    print("You entered:", chosen_character.lower())
