# Course: CS 30
# Period: 1
# Date created: 21/02/10
# Date last modified: 21/02/10
# Name: Janice Cotcher
# Description: Continous gameplay


# Map menu
def MapMenu():
    while True:
        print("\n" + 18 * "-" + "Map" + 18 * "-")
        x = input("North\nSouth\nWest\nEast\n\nExit\n\n")
        x = x.lower()
        if x == "north" or x == "south" or x == "west" or x == "east":
            print(f"\nYou moved {x}")
        elif x == "exit":
            break
        else:
            print("Thats not a direction you can move in try again")


# Inventory menu
def InvMenu():
    while True:
        print(("\n" + 15 * "-" + "Inventory" + 15 * "-"))
        x = input("Armour\nHealing\nWeapons\nTraps\n\nExit\n\n")
        x = x.lower()
        if x == "armour" or x == "armor":
            print("\nDisplays Armour")
        elif x == "healing":
            print("\nDisplays Healing items")
        elif x == "traps":
            print("\nDisplays Traps")
        elif x == "weapons":
            print("\nDisplays Weapons")
        elif x == "exit":
            break
        else:
            print("\nInvalid action try again")


# Main menu
while True:
    print(15*"-"+"Main Menu"+15*"-")
    x = input("Inventory\nMap\nQuit\nInteract\n\nExit\n\n")
    if x.lower() == "inventory":
        InvMenu()
    elif x.lower() == "map":
        MapMenu()
    elif x.lower() == "quit":
        break
    elif x.lower() == "interact":
        print("\nYou interacted with the environment")
    elif x.lower() == "exit":
        break
    else:
        print("\nInvalid action try again")
