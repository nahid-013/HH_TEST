import pytest

from  solution import sum_two, chek_bool, chek_str, chek_float

def test_int_one():
    assert sum_two(1,2) == 3

def test_int_two():
    assert sum_two(5,5) == 10

def test_int_three():
    with pytest.raises(TypeError) as error:
        sum_two(1, 2.4)
    assert 'Не верно введен тип аргумента' == error.value.args[0]


def test_bool_one():
    assert chek_bool(1,True) == 2

def test_bool_two():
    assert chek_bool(1,False) == 1



def test_str_one():
    assert chek_str('a','b') == 'ab'

def test_str_two():
    assert chek_str('sdsdsd','33443') == 'sdsdsd33443'

def test_str_three():
    with pytest.raises(TypeError) as error:
        chek_str(True, '2')
    assert 'Не верно введен тип аргумента' == error.value.args[0]

def test_float_one():
    assert chek_float(1.1,2.0) == 3.1

def test_float_two():
    assert chek_float(2.5,5.5) == 8

def test_float_three():
    with pytest.raises(TypeError) as error:
        chek_float(1.0, '2')
    assert 'Не верно введен тип аргумента' == error.value.args[0]

if __name__ == '__main__':
    pytest.main()