#!/usr/bin/python3

# repalce rpg starter project with this code when the new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Get to the Garden with a key and a potion to win! Avoid the monsters!.

    Commands:
        go [direction]
        get [item]
    ''')

def showStatus():
    #print the player's current status
    print('-------------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('You have ' + str(inventory) + ' in your inventory')
    #print an item if there is one
    if currentRoom == 'Hall':
        print('go south to enter the Kitchen')
        print('go east to enter the Dining Room')
        print('There is a key on the ground')
    if currentRoom == 'Dining Room':
        print('go west to enter the Hall')
        print('The room is empty, nothing to get')
    if currentRoom == 'Garden':
        print('go north to enter the Dining Room')
    print("-------------------------------")

#An inventory, which is initially empty
inventory=[]

#A dictionary linking a room to other rooms
rooms = {
    'Hall' : { 
        'south' : 'Kitchen',
        'east'  : 'Dining Room',
        'item'  : 'key'
        },

    'Kitchen' : {
        'north' : 'Hall',
        'item'  : 'monster',
        },
    'Dining Room' : {
        'west' : 'Hall'
        },
    'Garden' : {
        'north' : 'Dining Room'
        }
    }
    
#Start the player in the Hall
currentRoom='Hall'

showInstructions()
    
#Loop forever
while True:
    
    showStatus()

    #Get the player's next 'move'
    #.split() breaks it up into a list array
    #Eg typing 'go east' would give the list:
    #['go','east']
    move=''    
    while move == '':
        move = input('>')

    #Split allows an items to have a space on them
    #Get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    #If they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]   
        #there is no door (link) to the new room
        else:
            print('you can\'t that way!')

    #If they type 'get' first
    if move[0] == 'get':
        #If the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRooms] and move[1] in rooms[currentRoom]['item']:
            #Add the item to their inventory
            invetory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('you can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
