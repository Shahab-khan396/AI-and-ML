#Write a python program using function to convert Celsius to Fahrenheit.
def C_to_F(n):
    F=((((9/5)*n)+32))
    return F
c=int(input('Enter the celsius: '))
print(f"The fahrenheit is {C_to_F(c)}")