
class Employees ():
    name = "Areeb"
    company = "ITC"
    def emp_info(self):
        print(f"The name of employee is {self.name} and working in {self.company}")

class coders () :
    language = "Python"
    name = "Areeb"
    def coder_info(self) :
        print(f"The coder name is {self.name} and code in {self.language}")

class programmers(Employees, coders):
    name = "Areeb" 
    language = "Java"
    def pro_info(self):
        print(f"The name of programmer is {self.name} and working on {self.language}")


p1 = programmers()
p1.emp_info()
p1.coder_info()
p1.pro_info()


