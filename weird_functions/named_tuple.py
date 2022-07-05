#The accessing methods of NamedTuple

# import collections as col
# #create employee NamedTuple
# Employee = col.namedtuple('Employee', ['name', 'city', 'salary'])
# #Add two employees
# e1 = Employee('Asim', 'Delhi', '25000')
# e2 = Employee('Bibhas', 'Kolkata', '30000')
# #Access the elements using index
# print('The name and salary of e1: ' + e1[0] + ' and ' + e1[2])
# #Access the elements using attribute name
# print('The name and salary of e2: ' + e2.name + ' and ' + e2.salary)
# #Access the elements using getattr()
# print('The City of e1 and e2: ' + getattr(e1, 'city') + ' and ' + getattr(e2, 'city'))


#Conversion procedures of NamedTuple
import collections as col
#create employee NamedTuple
Employee = col.namedtuple('Employee', ['name', 'city', 'salary'])
#List of values to Employee
my_list = ['Asim', 'Delhi', '25000']
e1 = Employee._make(my_list)
print(e1)
#Dict to convert Employee
my_dict = {'name':'Bibhas', 'city' : 'Kolkata', 'salary' : '30000'}
e2 = Employee(**my_dict)
print(e2)
#Show the named tuple as dictionary
emp_dict = e1._asdict()
print(emp_dict)

import collections as col
#create employee NamedTuple
Employee = col.namedtuple('Employee', ['name', 'city', 'salary'])
#Add an employees
e1 = Employee('Asim', 'Delhi', '25000')
print(e1)
print('The fields of Employee: ' + str(e1._fields))
#replace the city of employee e1
e1 = e1._replace(city='Mumbai')
print(e1)