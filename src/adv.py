from room import Room
from player import Player
from item import Item

# Declare all items

apple = Item("Apple", "Apples are the ideal fruit to eat at any time")
sword = Item("Sword", "The blade has some moderate damage. It was crafted by Gino Minnelli , in the Heritu.")
dust = Item("Dust", "Could it be useful?")
coin = Item("Golden coin", "Some gold always can be handy")
helmet = Item("Helmet", "Protect your head is always a good idea")
tresure = Item("Hidden tresure", "Good thing you decided to search carefully and bring some light! Here it is behing big rock! Desired tresure!!!")


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     True,
                     [sword, apple]),

    'foyer':    Room("Foyer", 
                     "Dim light filters in from the south. Dusty passages run north and east.",
                     True,
                     [dust, coin]),

    'overlook': Room("Grand Overlook", 
                     "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", 
                     False,
                     [helmet, apple]),

    'narrow':   Room("Narrow Passage", 
                     "The narrow passage bends here from west to north. The smell of gold permeates the air.",
                     False,
                     [dust]),

    'treasure': Room("Treasure Chamber", 
                     "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
                     False,
                     [tresure]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

is_playing = True
help_message = """-----------------------------------------
To go North - enter 'n', East - 'e', South - 's', West - 'w'
To pick up an item - 'get [ITEM_NAME]'\nTo drop item - 'drop [ITEM_NAME]'
To see inventory - 'i'\nFor help message with instructions - 'h'\nTo quit the game - 'q'
-----------------------------------------"""

while is_playing:
    players_name = input("hello, stranger! What's your name: ")
    player = Player(players_name, room["outside"])
    print("Let me tell you how it works.")
    print(help_message)
    print(f"Right now you're at the {player.current_room.name}")
    print(player.current_room.description)
    while is_playing:
        user_action = input("What do you want to do? Answer: ")
        if user_action == "q":
            is_playing = False
        elif user_action == "h":
            print(help_message)
        elif user_action == 'i':
            if len(player.items) == 0:
                print("You are broke!")
            else:
                print("You have:")
                for item in player.items:
                    print(item.name)
        elif user_action[0] in ["n", "e", "s", "w"]:
            move_to = f"{user_action}_to"
            target_room = getattr(player.current_room, move_to)
            if target_room:
                player.current_room = target_room
                print(f"Right now you're at the {player.current_room.name}")
                print(player.current_room.description)
                user_action = input("Do you want to look around? Yes/No: ")
                if user_action.lower() == "yes":
                    print("You can see:")
                    for item in player.current_room.items:
                        print(item.name)
            else:
                print("You shall not pass!!! Ectually, there's nothing in this direction")  
        else:
            print("You shall not pass!!! Ectually, there's nothing in this direction")
        
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
