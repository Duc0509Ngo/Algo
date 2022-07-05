class Foo:

    def show(self):
        print('hi')

def add_attribute(self):
        self.z = 9

Test = type('Test', (Foo,), {'x': 1, 'add_attribute': add_attribute})
t = Test()
t.add_attribute()
print(t.z)


