import datetime

class Employee:
    num_of_emps = 0
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1
    
    
    @classmethod    #only access states of the class: num_of_emps and raise_amt 
    def from_string(cls, str_):
        first, last, pay = str_.split('-')
        
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        print(day.weekday())
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


e1 = Employee.from_string('Duc-Ngo-5000')
my_date = datetime.date(2019, 7, 13)
print(Employee.is_workday(my_date))