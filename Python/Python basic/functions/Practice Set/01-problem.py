def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c>a and c>b:
        return c

a = input('Enter 1st Number:  ')
b = input('Enter 1st Number:  ')
c = input('Enter 1st Number:  ')

print("The greatest number is:", greatest(a, b, c))
