# I made this with the hopes of increasing my typing speed with numbers

import random
import time

def main():
    start_time = time.time()
    
    end_time = start_time + 60
    
    number_correct = 0
    
    while time.time() < end_time:
    
        a = random.randrange(9)
        b = random.randrange(9)
        
        answer = int(a * b)
        
        guess = int(input(f"{a} x {b} = "))
        
        if answer == guess:
            number_correct += 1
            
    print(f"Your total score is: {number_correct}")
    

if __name__ == "__main__":
    main()