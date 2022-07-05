from library import Base

class Derived(Base):
    def bar(self):
        return self.foo()

assert hasattr(Derived, "salary")
d1 = Derived()
print(d1.bar())