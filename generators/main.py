import sys
# class Gen:
#     def __init__(self, n):
#         self.n = n
#         self.last = 0
    

#     def __next__(self):
#         return self.next()
#     def next(self):
#         if self.last == self.n:
#             raise StopIteration()
        
#         rv = self.last ** 2
#         self.last += 1
#         return rv
    
# g = Gen(100)
# while True:
#     try:
#         print(next(g)).        #next will call __next__ (dunder method)
#     except StopIteration:
#         break

def gen(n):
    for i in range(n):
        yield i**2

x = [i**2 for i in range(10000)]

g = gen(10000)
print(next(g))
print(sys.getsizeof(x))

print(sys.getsizeof(g))


