# Generate random number 1 - 75 Bingo numbers
# Ask "Do you want to pick a random number? (Y/N)"
# Y -> generate random number
# After, the list of picked and available numbers is updated
# picked numbers are grouped B-I-N-G-O
# B = 1 - 15, I = 16 - 30, N = 31 - 45, G = 46 - 60, O = 61 - 75
# If N is inputted at any point, the game will stop
# After N, "Do you want another set of bingo game? (Y/N)"
# Y -> Repeat -> all available and picked list will be reset
# N -> Stop program

import random
import time

def inputHandler(USER_INPUT):
    match (USER_INPUT):
        case 'Y':
            return True
        case 'N': 
            return False
        case _:
            return "Invalid"

print("                             Welcome to buBINGO\n")
print("Starting a game....")

ALL_NUMBERS = []
B_NUMBERS = []
I_NUMBERS = []
N_NUMBERS = []
G_NUMBERS = []
O_NUMBERS = []
RANDOM_NUMBER = 0

while True:
    
    for num in range(1 , 76):
        ALL_NUMBERS.append(num)
    
    for row in range(len(ALL_NUMBERS)):
        print(ALL_NUMBERS[row], end= ", ")

    userInput = input("Do you want to pick a random number? (Y/N)").capitalize()

    print("\n                       Available Numbers")
    print("                     B =", str(ALL_NUMBERS[0:15])[1:-1])
    print("                     I =", str(ALL_NUMBERS[15:30])[1:-1])
    print("                     N =", str(ALL_NUMBERS[30:45])[1:-1])
    print("                     G =", str(ALL_NUMBERS[45:60])[1:-1])
    print("                     O =", str(ALL_NUMBERS[60:75])[1:-1])
    
    INPUT_CONDITION = inputHandler(USER_INPUT = userInput)
    
    match INPUT_CONDITION:
        case True:
            RANDOM_NUMBER = random.choice(ALL_NUMBERS)
            print("Drawn number:", RANDOM_NUMBER)
            
        case False:
            print("Ending game...")
            time.sleep(1.5)
            userInput = input("Do you want another set of bingo game? (Y/N)")
            inputHandler(USER_INPUT = userInput)
            
            if True:
                continue
            else:
                print("Closing program...")
                time.sleep(1.5)
                print("Program closed.")
                break
    
    if RANDOM_NUMBER 
    B_NUMBERS.append()
                    

        
                
        
    