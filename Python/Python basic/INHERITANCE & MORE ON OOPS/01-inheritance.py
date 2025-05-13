# class employee:
#     name ="shahab khan"
#     roll_no=221396

# class programmer(employee):
#     language="python"
    
    
# a=employee()
# b=programmer()
# print(a.name)
# print(a.roll_no)  
# print(b.language)  
# print(b.name)     
#-------------------------------------------------------------------------------------------------

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)