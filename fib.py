def fib_sequence(x, y, i, first_call):
    if first_call:
        print(x)
        print(y)
        first_call = False
    
    if i == 0:
        pass
    
    else:
        f_one = x
        f_two = y

        sum = f_one + f_two
        
        print(sum)
        
        i -= 1
        
        fib_sequence(f_two, sum, i, first_call)



def main():
    f_one = 0
    f_two = 1
    i = 20
    firstCall = True
    
    print(f"The Fibonacci Sequence is for the first {i} terms is... ")
    fib_sequence(f_one, f_two, i, firstCall)
    
if __name__ == "__main__":
    main()