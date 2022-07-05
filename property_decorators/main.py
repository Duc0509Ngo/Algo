from abc import abstractproperty
from dataclasses import dataclass

from attr import field


@dataclass
class Employee:
    first: str = field(default='David')
    last: str = field(default='Nau')
    

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
    @classmethod
    def func(cls):
        print(cls.first)
           
emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schafer'

del emp_1.first, emp_1.last

del emp_1.fullname



