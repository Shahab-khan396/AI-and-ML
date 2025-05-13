import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("guess the number: "))
    if(a>n):
        print("Lower Number Please: ")
    else:
        print("Higher Number Please: ")
    
print(f"You have guess the {n} number correctly in {guesses} attempts ")
    