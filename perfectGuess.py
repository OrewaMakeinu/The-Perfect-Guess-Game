import random
n = random.randint(1,100)
a = -1
guesses = 1
while (a!= n):

    
    if(guesses > 5):
            print("Chances Over!")
            print(f"The correct number was: {n}")
            break
    
    a = int(input("Guess The Number: "))
    
    if(a > n):
        print("Lower Number Please:")
    elif(a < n):
        print("Higher Number Please:")
    guesses += 1
    if(a == n):
        print(f"Show the Score {guesses}")
