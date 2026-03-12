import random 

def dice_rolling_game():
    print("Welcome to the dice rolling game.")
    
    rounds=int(input("How many times you want to play?:"))
    results=[]
   
    for i in range(1,rounds+1):
        roll=random.randint(1,6)
        results.append(roll)
       
    print("\nHere are your dice rolls:")
    print(results)
    print("Game Over! 🎉")

dice_rolling_game()
        
