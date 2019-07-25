a = lambda x : 2*x+3
print(a(3))
try:
    raise Exception
    print('lll')
except Exception as e:
    print(type(e))