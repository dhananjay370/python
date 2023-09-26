class Employee:
    company = "Apple"

    def show(self):
        print(f"The Name is {self.name} and the company is {self.company}")

    @classmethod
    def changeCompany(cls, newcompany):
        cls.company = newcompany


e1 = Employee()
e1.name = "Dhananjay"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
