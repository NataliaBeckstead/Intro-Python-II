import random

from room import Room
from player import Player
from item import Item
from rock_game import rock_paper_scissor_game

# Declare all items

apple = Item("apple", "Apples are the ideal fruit to eat at any time")
sword = Item("sword", "The blade has some moderate damage. It was crafted by Gino Minnelli , in the Heritu.")
dust = Item("dust", "Could it be useful?")
coin = Item("coin", "Some gold always can be handy")
helmet = Item("helmet", "Protect your head is always a good idea")
tresure = Item("tresure", "Good thing you decided to search carefully and bring some light! Here it is behing big rock! Desired tresure!!!")


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
To pick up an item - 'get [ITEM_NAME]' or 'take [ITEM_NAME]'
To drop item - 'drop [ITEM_NAME]'
To look around - 'look'
To see inventory - 'i'\nFor help message with instructions - 'h'\nTo quit the game - 'q'
-----------------------------------------"""
# "Let there be LIGHT!"

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
        elif user_action == 'look':
            if player.current_room.is_light:
                if len(player.current_room.items) > 0:
                    print("You can see:")
                    for item in player.current_room.items:
                        print(item.name)
                else:
                    print("The room is empty.")
            else:
                print("It's too dark here. Can't see anything.")
        elif user_action[0] in ["n", "e", "s", "w"]:
            move_to = f"{user_action}_to"
            target_room = getattr(player.current_room, move_to)
            if target_room:
                player.current_room = target_room
                print(f"Right now you're at the {player.current_room.name}")
                print(player.current_room.description)
                if random.randint(1,3) == 1:
                    print("You met a stranger!")
                    answer = input("Do you want to play with him? yes/no: ")
                    if answer == "yes":
                        if rock_paper_scissor_game():
                            print("You won!!!")
                        else:
                            print("You've lost. Maybe next time")
            else:
                print("You shall not pass!!! Ectually, there's nothing in this direction")  
        elif user_action.startswith("get "):
            i = 0      # checking if we was able to get anything
            for item in player.current_room.items:
                    if item.name == user_action[4:]:
                        print(f"{user_action[4:]} is now yours!")
                        player.items.append(item)
                        player.current_room.items.remove(item)
                        i +=1
            if i == 0:
                print("You can't get this")
        elif user_action.startswith("take "):
            i = 0      # checking if we was able to get anything
            for item in player.current_room.items:
                    if item.name == user_action[5:]:
                        print(f"{user_action[5:]} is now yours!")
                        player.items.append(item)
                        player.current_room.items.remove(item)
                        i +=1
            if i == 0:
                print("You can't get this")
        elif user_action.startswith("drop "):
            i = 0      # checking if we was able to drop anything
            for item in player.items:
                    if item.name == user_action[5:]:
                        print(f"You get rid of {user_action[5:]}!")
                        player.items.remove(item)
                        player.current_room.items.append(item)
                        i +=1
            if i == 0:
                print("You don't have it")
        else:
            print("You shall not pass!!! Ectually, there's nothing in this direction")

""" TODO:
add a randomly showing up stranger
If he show up - he offers to play rock scissors paper
If user won first time  -  give him a lanter

"""