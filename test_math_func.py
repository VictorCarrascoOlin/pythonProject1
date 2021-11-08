import math_func
import pytest
import sys


class TestMath:
    @pytest.mark.addition
    def test_add(self):
        assert math_func.add(7, 3) == 10
        assert math_func.add(7) == 9
        assert math_func.add(5) == 7


class TestMath2:

    def test_product(self):
        assert math_func.product(5, 5) == 25
        assert math_func.product(5) == 10
        assert math_func.product(7) == 14
        print(math_func.division(10, 2))

    @pytest.mark.division
    def test_division(self):
        assert math_func.division(18, 2) == 9


#@pytest.mark.string
#def test_add_strings():
#    result = math_func.add('Hello ', 'World')
#    assert result == 'Hello World'
#    assert type(result) is str
#    assert 'Heldlo' not in result


#@pytest.mark.string
#def test_product_strings():
#    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
#    result = math_func.product('Hello ')
#    assert result == 'Hello Hello '
#    assert type(result) is str
#    assert 'Hello' in result
