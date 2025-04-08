'''
DOC STRING
Adventure Game
Author: Shambhavi Koirala
Version: 2.2
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''
#---------------------------------------------------------------------
# Player class to store player info and game state
#---------------------------------------------------------------------

class Player:
    # initializer/constructor
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# --------------------------------------------------------------------
# Function : welcome_player
# Greet the player, ask for their name and return the name as a string
# --------------------------------------------------------------------

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")

    # Ask for the player's name
    name = input("What is your name, adventurer?")
    player = Player(name)

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player.name}! Your journey begins now.")

    return player

# --------------------------------------------------------------------
# Function : describe_area
# Print the opening description of the area
# --------------------------------------------------------------------

def describe_area():
    # Describe the starting area
    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown...
    """)
    
# --------------------------------------------------------------------
# Function : add_to_inventory
# Accepts an item as a parameter
# Adds it to the inventory list and confirm the pickup to the player
# --------------------------------------------------------------------

def add_to_inventory(item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

# --------------------------------------------------------------------
# Game starts here
# Call the welcome and describe area functions
# --------------------------------------------------------------------

player = welcome_player()
describe_area()

# --------------------------------------------------------------------
# TODO: Commit with a message like:
#       REF unlock new areas based on inventory items
# TODO: Push your commits to GitHub
# --------------------------------------------------------------------



# --------------------------------------------------------------------
# Main game loop
# Run this until the player quits


# TODO: Inside the game loop:
#       - If the user chooses option 2, call add_to_inventory("map")

# Start the game Loop
while True: 
    print("\nYou see two path ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Take the straight path into the cave.")
    print("\t4. Explore the nearby cave.")
    # TODO: Add a new menu option for "Explore a nearby cave"

    print("\t5. Stay where you are.")

    print("\tType 'i' to view your inventory.")
    # TODO update numbers
    decision = input("What will you do (1,2,3,4,5 or i): ").lower()

    # open the inventory
    if decision == "i":
        print("Inventory", player.inventory)
        continue

    if decision == "1":
        print(f"{player.name}, you step into the dark woods. The trees whisphered as you walk deeper.")
        add_to_inventory("lantern")
        player.has_lantern = True

    elif decision == "2":
        print(f"{player.name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("map")
        player.has_map = True

    elif decision == "3":
        if player.has_lantern:
            print(f"{player.name}, you see two paths ahead")
            print("Inside the cave, you have hidden treasure.")
            add_to_inventory("treasure")
            print("You have picked up a lantern!")
            # TODO: After picking up new items, confirm to the player they got it
            # add to inventory
        
        else:
            print("Its too dark to continue without a lantern.")
            print("Maybe you find a light source to move ahead!")

    # TODO: In the valley choice:
#       - If player.has_map is True: allow entry and add "rare herbs" to inventory
#       - Else: display a message that you can’t find the valley
# TODO: After picking up new items, confirm to the player they got it
# add to inventory

    # TODO update numbers
    # Stay where you are

    elif decision == "4":
        if player.has_map:
            print("You enter a beautiful secret valley full of trees and plants.")
            print(f"{player.name}, you have found some rare herbs.")
            add_to_inventory("rare herbs")
        else:
            print("You are lost in the cave wandering in circles. Try finding a map! ")

    elif decision == "5":
        print("You stay still listening to the "
              "distant sounds of the forest")
    else:
        print("Invalid choice. Please choose "
              "1, 2, 3, 4, 5.")

    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break # Exit the loop and end the game
