# from contextlib import contextmanager
# with open('hello.txt', 'w') as f:
#     f.write('Hello World!')
    
    
# print(f.closed)


# @contextmanager
# def open_file(name):
#     f = open(name, 'w')
#     try:
#         yield f
#     finally:
#         f.close()

try:
    f = open('hello.txt', 'w')
finally:
    f.close()
print(f.closed)