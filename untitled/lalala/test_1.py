import pytest

@pytest.fixture()
def a1():
    a = 'leo'
    b = '123456'
    print('传出a,b')
    return (a, b)

def test2(a1):
    u = a1[0]
    p = a1[1]
    assert u == 'leo'
    assert p == '123456'
    print('元祖形式正确')

if __name__ == '__main__':
    pytest.main('test_anster.py')
