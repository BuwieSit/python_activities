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


def inputHandler(USER_INPUT):
    match (USER_INPUT):
        case 'Y':
            return True
        case 'N': 
            return False
        case _:
            return "Invalid"


allNum = []

for num in range(1 , 76):
    allNum.append(num)

print("                             Welcome to buBINGO\n")
print("Starting a game....")


