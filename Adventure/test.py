name = "ADVENTURER"

print("Welcome adventurer, what is your name?")
name = input()

print("Welcome " + name + ", you are about to embark on a great adventure.")
print("You are standing in front of a castle. Do you want to enter the castle or go to the forest?")

choice = input()
if choice == "castle":
    print("The Dragon ate you!")
    print("Game Over!")
else:
    print("Hmm now what?")
