print("Welcome to trasure island")
print("Your mission is to find the treasure")

choice1 = input('You are at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across \n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n').lower()
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")