def test1(item):
    print('ok')
    print(item)

def make_callable(str):
    if str == 'test1':
        return test1(str)

t = make_callable('test1')
print(type(t))
t()