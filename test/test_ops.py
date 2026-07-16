import pytest
from calc.ops import add, multiply

@pytest.mark.parametrize( 
    "a,b,expected",
    [
        (1,2,3),
        (-5,5,0),
        (2.5,0.5,3.0),
        (0,0,0),
        (10,-3,7)
    ],
)

def test_add(a,b,expected):
    assert add(a,b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1,2,2),
        (3,4,12),
        (-5,5,-25),
        (3,9,27),
        (9,-8,-72)
    ]
)
def test_multiply(a,b,expected):
    assert multiply(a,b) == expected