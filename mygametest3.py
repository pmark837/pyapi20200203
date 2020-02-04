#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
    RPG Escape Game
    ========
    Search for the magic potion and escape! Beware of monsters!.

    Commands:
        go [direction]
        get [item]
    ''')

def showStatus():
    #print the player's current status
    #print('\n-------------------------------\n')
    print(f"\n-------------------------------\nYou are in the  {currentRoom}")
	
    #print the current inventory
    print(f"You have {inventory} in your inventory\n")

    #Display instructions depending on the room
    if currentRoom == 'Hall':
        #print('Go south to enter the Kitchen')
        #print('Go east to enter the Dining Room')
        #print('')
        #print('There\'s ' + rooms[currentRoom]['item'] + ' on the ground')
        #converted to f string formati
        print(f"Go south to enter the Kitchen\nGo east to enter the Dining Room\n\nThere\'s {rooms[currentRoom]['item']} on the ground")
    
    if currentRoom == 'Dining Room':
        #print('Go west to enter the Hall')
        #print('Go south to enter the Garden')
        #print('')
        #print('There\'s ' + rooms[currentRoom]['item'] + ' in the corner')
        print(f"Go west to enter the Hall\nGo south to enter the Garden\n\nThere\'s {rooms[currentRoom]['item']} in the corner")       
    
    if currentRoom == 'Garden':
        print(f"Go north to go back to the Dining Room\nThere is a gate in the far end that leads outside but it is locked..\n")
        
        if (('key' in inventory) and ('potion' in inventory)):
            print('You found the Magic potion and also unlocked the gate with the key!... YOU WIN!')
            return True
            
        elif ('key' in inventory) and ~ ('potion' in inventory):
            print('You found the key to unlock the gate but you have not found the potion!\nKeep looking!...')
        
        else:
            print('Looks like you need something to unlock it\nThe garden is pretty empty, there is nothing to get')
		
    print("\n-------------------------------\n")
    return False

#an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'a key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'a potion'
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
  
  if showStatus():
      break


  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
      move = input('What would you like to do? ')

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
      inventory += [move[1].lstrip('a ')]
	  
      #display a helpful message
      print(move[1] + ' picked up!')
	  
      #Set item of the current room to "nothing" since it's been picked up
      rooms[currentRoom]['item'] = 'nothing'
	  
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
	  
## If a player enters a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('As you enter the Kitchen a monster comes at you... GAME OVER!')
    break
	  
  ## Define how a player can win
  #if (currentRoom == "Garden") and ("a key" in inventory and "a potion" in inventory):
  #    print("You found the Magic potion and also unlocked the gate with the key YOU WIN!")
  #else:
  #    print("You are missing some things...")
  
  #if (currentRoom == 'Garden') and ('a key' in inventory) and ('a potion' not in inventory):
  #      print('You found the key to unlock the gate but you have not found the potion!')
  #      print('Keep Looking...')
  #elif (currentRoom == 'Garden') and ('a key' in inventory and 'a potion' in inventory):
  #      print('You found the Magic potion and also unlocked the gate with the key!... YOU WIN!')
  #      break
