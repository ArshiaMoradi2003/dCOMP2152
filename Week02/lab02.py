# Import the random library to use for the dice later
import random

# Define Variables
diceOptions = [1, 2, 3, 4, 5, 6]
combatStrength = int(input("Enter your combat Strength: "))

# Define the weapons array with increasing levels of strength
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Input for the dice roll to choose the weapon
try:
    input("Roll the dice (Press enter) to choose your weapon...")
    weaponRoll = random.choice(diceOptions)  # Randomly choose a number between 1 and 6
    print("You rolled a " + str(weaponRoll) + " for your weapon")

    # Add the weaponRoll to the combat strength
    combatStrength += weaponRoll

    # Use weaponRoll as an index into the weapons array and print out the weapon name
    weapon = weapons[weaponRoll - 1]
    print("Your weapon is: " + weapon)

    # Define the conditions based on the weapon rolled
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # If the weapon is not "Fist", print out a thank you message
    if weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError:
    print("Error: Please enter a valid integer.")
    exit()
except IndexError:
    print("Error: Invalid weapon roll.")
    exit()

# Print the final combat strength
print("Your final combat strength is: " + str(combatStrength))