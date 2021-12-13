def test1():
    print('ok')

def make_callable(str):
    if str == 'test1':
        return test1

t = make_callable('test1')
print(type(t))
t()