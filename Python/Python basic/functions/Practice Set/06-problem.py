def inch_to_cms(n):
    inch=n*2.54
    return inch
n=int(input("Enter the inches:   "))
print(f"{n} inches = {inch_to_cms(n)} centimeter  ")