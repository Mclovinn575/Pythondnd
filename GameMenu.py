import os



def Clear():
    os.system('clear')

def Menu():
    Clear()
    print("1. New Game")
    print("2. Load Game")
    print("3. About")
    print("4. Exit")
    c = input("> ")
    match c:
        case "1":
            NewGame()
        case "2":
            LoadGame()
        case "3":
            About()
        case "4":
            Exit()
    

def NewGame():
    Clear()
    print("Starting...")
    input()

def LoadGame():
    Clear()
    print("Loading...")
    input()

def About():
    #Put in details about the game.
    Clear()
    print("This is the ABOUT page!")
    input()

def Exit():
    exit()







