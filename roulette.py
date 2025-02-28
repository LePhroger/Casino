import random as rd

RED = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
BLACK = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

Player_input = 0
Win_number = 0
Win_colour = ""

Active = True

while Active:
    Player_input = input("What is your bet (1-36)?")

    Win_number = rd.randint(1,36)


    if Win_number in RED:
        Win_colour = "RED"
    elif Win_number in BLACK:
        Win_colour = "BLACK"

    if Player_input.isdigit(): 
        pass
    print("The winning number is",Win_number,Win_colour)

    if Win_number == Player_input:
        print('Winner')
    else:
        print('Loss')        