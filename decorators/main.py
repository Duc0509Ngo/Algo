def func(f):

    def wrapper(*args, **kwargs):
        print('Started')
        value = f(*args, **kwargs)
        print('Finished')
        return value

    return wrapper

@func
def func2(x):
    return x

@func
def func3():
    print('I am func3')

func2(3)


