import random
import time

def inputHandler(USER_INPUT):
    match (USER_INPUT):
        case 'Y': return True
        case 'N': return False
        case _: return None

print("                             Welcome to buBINGO\n")
print("Starting a game....")

ALL_NUMBERS = []
B_NUMBERS = []
I_NUMBERS = []
N_NUMBERS = []
G_NUMBERS = []
O_NUMBERS = []
RANDOM_NUMBER = 0

for num in range(1 , 76):
    ALL_NUMBERS.append(num)
        
while True:
    print("\n                       Available Numbers")
    print("                     B =", str(ALL_NUMBERS[0:15])[1:-1])
    print("                     I =", str(ALL_NUMBERS[15:30])[1:-1])
    print("                     N =", str(ALL_NUMBERS[30:45])[1:-1])
    print("                     G =", str(ALL_NUMBERS[45:60])[1:-1])
    print("                     O =", str(ALL_NUMBERS[60:75])[1:-1])
    time.sleep(1)
    print("\n                       Picked Numbers")
    print("                     B =", str(B_NUMBERS)[1:-1])
    print("                     I =", str(I_NUMBERS)[1:-1])
    print("                     N =", str(N_NUMBERS)[1:-1])
    print("                     G =", str(G_NUMBERS)[1:-1])
    print("                     O =", str(O_NUMBERS)[1:-1])
    time.sleep(1)
    
    userInput = input("\nDo you want to pick a random number? (Y/N): ").capitalize()
    INPUT_CONDITION = inputHandler(USER_INPUT = userInput)
    
    if INPUT_CONDITION is None:
        print("\n*Unknown Command. Continuing...*")
        time.sleep(1)
        continue
    
    match INPUT_CONDITION:
        
        case True:
            RANDOM_NUMBER = random.choice(ALL_NUMBERS)
            time.sleep(1.5)
            print("Drawn number:", RANDOM_NUMBER)

        case False:
            print("Ending game...")
            time.sleep(1.5)

            userInput = input("Do you want another set of bingo game? (Y/N): ").capitalize()
            INPUT_CONDITION = inputHandler(userInput)
            
            if INPUT_CONDITION is None:
                print("\n*Unknown Command. Continuing...*")
                time.sleep(1)
                continue

            if INPUT_CONDITION is True:
                B_NUMBERS.clear()
                I_NUMBERS.clear()
                N_NUMBERS.clear()
                G_NUMBERS.clear()
                O_NUMBERS.clear()
                ALL_NUMBERS.clear()
                for num in range(1, 76):
                    ALL_NUMBERS.append(num)
                continue

            if INPUT_CONDITION is False:
                print("Closing program...")
                time.sleep(1.5)
                print("Program closed.")
                break
            
    if RANDOM_NUMBER >= 1 and RANDOM_NUMBER <= 15:
        B_NUMBERS.append(RANDOM_NUMBER)
        ALL_NUMBERS.remove(RANDOM_NUMBER) 
        time.sleep(1)
        print("\nRandom Selected Number: B", str(RANDOM_NUMBER))
        continue
        
    elif RANDOM_NUMBER >= 16 and RANDOM_NUMBER <= 30:
        I_NUMBERS.append(RANDOM_NUMBER)
        ALL_NUMBERS.remove(RANDOM_NUMBER)
        time.sleep(1)
        print("\nRandom Selected Number: I", str(RANDOM_NUMBER))
        continue
        
    elif RANDOM_NUMBER >= 31 and RANDOM_NUMBER <= 45:
        N_NUMBERS.append(RANDOM_NUMBER)
        ALL_NUMBERS.remove(RANDOM_NUMBER)
        time.sleep(1)
        print("\nRandom Selected Number: N", str(RANDOM_NUMBER))
        continue
        
    elif RANDOM_NUMBER >= 46 and RANDOM_NUMBER <= 60:
        G_NUMBERS.append(RANDOM_NUMBER)
        ALL_NUMBERS.remove(RANDOM_NUMBER)
        time.sleep(1)
        print("\nRandom Selected Number: G", str(RANDOM_NUMBER))
        continue
        
    elif RANDOM_NUMBER >= 61 and RANDOM_NUMBER <= 75:
        O_NUMBERS.append(RANDOM_NUMBER)
        ALL_NUMBERS.remove(RANDOM_NUMBER)
        time.sleep(1)
        print("\nRandom Selected Number: O", str(RANDOM_NUMBER))
        continue

                
        
    