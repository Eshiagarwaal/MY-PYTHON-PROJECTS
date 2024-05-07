#THIS IS A GAME THAT I HAVE BUILT IN PYTHON! LET'S GET STARTED WITH IT
print("Welcome to the treasure island. \nYour mission in this game is to find the treasure. \nso Let's get started.")
print("You have started your journey on the treasure island. This island is full of adventures and mystery. One wrong step and the game is over for you. Wait you just came across a crossroad")
direction = input("Enter the direction you would like to go in? left or right : ")
if direction == "left":
    swim_or_wait = input("Now after taking a left you came across a river. \nThis river could be filled with some dangerous aquatic animals. \nWhat would you like to do wait for the boat to come or swim across? type 'wait' for waiting for the boat or type 'swim' for swimming across the river: ")
    if swim_or_wait == "wait":
       color = input("After crossing the river you are on the final stage of this treasure hunt. \nNow you have three doors in front of you of red, yellow and blue color. \nWhich door would you like to unlock red, yellow or blue : ")
       if color == "red" :
            print("Oops! you unlocked the door full of snakes. Game over")
       elif color == "blue":
        print("Oops! You unlocked a door full of dacoits. Game over")
       elif color == "yellow":
        print("Hurray! you have unlocked the right door. \ncongratulations on winning the treasure.")
       else:
        print("Oops! You have chosen a door that doesn't exist. Game over")
    else:
        print("Oops! You entered a river full crocodiles. Game over")
else:
    print("You have taken a route full of problems like fire, thorns,dacoits, etc. Game over ")