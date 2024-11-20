import pytest

from  solution import fetch_animal_counts

def test_task2_one():
    with pytest.raises(AttributeError) as error:
        fetch_animal_counts('https://ru.wkipedia.org/wiki/Категория:Животные_по_алфавиту')
    assert "'NoneType' object has no attribute 'find_all'" == error.value.args[0]

def test_task2_two():
    with pytest.raises(AttributeError) as error:
        fetch_animal_counts('https://ru.wikipedia.org/wiki/Категория:_алфавиту')
    assert "'NoneType' object has no attribute 'find_all'" == error.value.args[0]

if __name__ == '__main__':
    pytest.main()