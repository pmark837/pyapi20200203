#!/usr/bin/python3

# repalce rpg starter project with this code when the new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
        go [direction]
        get [item]
    ''')

    def showStatus():
        #print the player's current status
        print('---------------------------')
        print('You are in the ' + currentRoom)
        #print the current inventory
        print('Inventory: ' + str(inventory))
        #print an item if there is one
        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])
        print("-------------------------------")

    #an inventory, which is initially empty
    inventory=[]

    #a dictionary linking a room to other rooms
    rooms={
            'Hall':{
                
