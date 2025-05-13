name=input("Enter Your name \n")
date=input("enter the date to selected \n")
letter = ''' Dear <|Name|>, You are selected! \n <|Date|> '''
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))
