# L1: DATA TYPES AND VARIABLES -----------------------------------------------------------------

# Data Types:
# There are different types of data that we can store in a variable.
# int   - Integer   - 10
# float - Decimal   - 3.14
# str   - String    - "Hello World"
# bool  - Boolean   - True or False

# Variables:
# Variables are used to store data.
# x = 10
# y = 20
# z = x + y

# Goal:
# Create the following variables:
# Lives
Lives = 3

# Name
# -- CODE HERE --

# Alive
Alive = True

# Score
# -- CODE HERE --

# Winner (Default should be False)
# -- CODE HERE --



# L2: INPUT AND OUTPUT -------------------------------------------------------------------------
# To print a message to the console, use the print() function.
print("Hello World")
# Create a message to greet the player and ask for their name.
# -- CODE HERE --

# We can create or update a variable's value by asking the user for input.
Name = input()

# Let's print the player's name.
print("Welcome", Name, ", you are about to embark on a great adventure.")


# Let's also adjust how many lives the player has.
print("How many lives do you want?")
# code the line that updates the lives variable
# -- CODE HERE --

# Then confirm the number of lives.
print("You have", Lives ,"lives.")





# L3: CONDITIONALS ---------------------------------------------------------------------------
# Conditionals are used to make decisions in code.
print("Do you want to go to the castle or the forest?")
choice = input()
if choice == "castle":
    print("The Dragon ate you!")
    print("Game Over!")
else:
    print("Hmm now what?")

# Create your own conditional statement with more than one option.
# -- CODE HERE --




# L4: ADVANCED CONDITIONALS ------------------------------------------------------------------
# We can use elif to check multiple conditions.
print("What kind of weapon do you want? Sword, Bow, or Magic?")
weapon = input()
if weapon == "Sword":
    print("You have a sword.")
elif weapon == "Bow":
    print("You have a bow.")
elif weapon == "Magic":
    print("You have magic.")
else:
    print("You have no weapon.")

# Create your own advanced conditional statement with more than two options.
# -- CODE HERE --





# L5: For Loop -------------------------------------------------------------------------------
# For loops are used to repeat code a certain number of times.
for number in range(5):
    print(number)

# Create a For loop that prints how many lives you have left.
# -- CODE HERE --






# ---------------------------------------------------------------------------------------------
# For loops are used to repeat code a certain number of times.
for life in range(Lives):
    print("You have", Lives - life, "lives left.")
else:
    print("You have no lives left. GAME OVER")






# L6: While Loop -----------------------------------------------------------------------------
# While loops are used to repeat code until a condition is met.
for life in range(Lives):
    print("You have", Lives - life, "lives left.")
    while Alive:
        print("You are alive.")
        Alive = False
else:
    print("You have no lives left. GAME OVER")






# L7: CREATE THE LEVELS -----------------------------------------------------------------------
for life in range(Lives):
    # Go back to Level 1
    Level = 1
    Alive = True
    print("You have", Lives - life, "lives left.")
    while Alive:
        if Level == 1:
            print("Punch or Run")
            choice = input()
            if choice == "Punch":
                print("The dragon ate you!")
                Alive = False
            else:
                print("Nice you found cover!")
                Level = 2
        
        elif Level == 2:
            print("Grab Shield or Sword")
            choice = input()
            if choice == "Shield":
                print("Good Choice!")
                Level = 3
            else:
                print("The dragon had a feeling you would do that.")
                print("The dragon ate you!")
                Alive = False

        elif Level == 3:
            print("Use your Weapon or Shield")
            choice = input()
            if choice == "Weapon":
                print("Not so fast! The Dragon breathes fire and you are toast!")
                Alive = False
            else:
                print("You blocked the fire with your shield and the dragon is stunned!")
                Level = 4
        
        elif Level == 4:
            print("Finish the dragon or run")
            choice = input()
            if choice == "Finish":
                print("You defeated the dragon!")
                Win = True
                break
            else:
                print("You are not that fast and the dragon eats you!")
                Alive = False
 
else:
    print("You have no lives left. GAME OVER")


# L8: Win Condition --------------------------------------------------------------------------
if Win:
    print("Congratulations! You have defeated the dragon and saved the kingdom!")