class Employee:
    def __init__(self, Qua=None, Name=None, Age=None, Pro=None):
        self.name = Name
        self.age = Age
        self.qualification = Qua
        self.job = Pro

    def __str__(self):
        return f"Name: {self.name}, {self.age}, {self.qualification}, {self.job}"

    def set_data(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.qualification = input("Enter your qualification: ")
        self.job = input("Enter your job: ")

if __name__ == '__main__':
    employees = []
    for i in range(5):
        emp = Employee()
        emp.set_data()
        employees.append(emp)

    for emp in employees:
        print(emp)