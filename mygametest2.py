#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

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
    
	#Display instructions depending on the room
    if currentRoom == 'Hall':
        print('go south to enter the Kitchen')
        print('go east to enter the Dining Room')
        print('There is a '+ str(rooms[currentRoom]['item']) + ' on the ground')

    if currentRoom == 'Dining Room':
        print('go west to enter the Hall')
        print('go south to enter the Garden')
        print('There is a ' + str(rooms[currentRoom]['item']) + ' in the corner')
                
    if currentRoom == 'Garden':
        print('go north to enter the Dining Room')
        print('The room is empty, nothing to get')
		
    print("-------------------------------")

#an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
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
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
				},
            'Garden' : {
                  'north' : 'Dining Room'
				}
         }
		 
#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
	
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
	  
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
	  
      #display a helpful message
      print(move[1] + ' picked up!')
	  
      #delete the item from the room
      del rooms[currentRoom]['item']
	  
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
	  
## If a player enters a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('Looking around you see something in the corner, the monster charges and attacks you... GAME OVER!')
    break
	  
## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
	
	
