import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    assert utils.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    assert utils.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    assert utils.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    assert utils.divide(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 0, "Cannot divide by zero."), (2, 0, "Cannot divide by zero.")],
)
def test_divide_by_zero(a, b, expected):
    with pytest.raises(ValueError) as excinfo:
        utils.divide(a, b)
    assert str(excinfo.value) == expected


@pytest.mark.parametrize(
    "a, expected", [(0, 0), (1, 1), (2, 10), (3, 11), (4, 100), (5, 101)]
)
def test_binary(a, expected):
    assert utils.binary(a) == expected


@pytest.mark.parametrize(
    "a, expected",
    [(1100, "Cannot convert number over 100"), (0, "Cannot convert 0 to binary")],
)
def test_binary_invalid(a, expected):
    with pytest.raises(ValueError) as excinfo:
        utils.binary(a)
    assert str(excinfo.value) == expected


@pytest.mark.parametrize(
    "a, expected",
    [
        (-1, "Cannot convert not natural number"),
        (0.5, "Cannot convert not natural number"),
        (5.123, "Cannot convert not natural number"),
    ],
)
def test_binary_is_natural(a, expected):
    with pytest.raises(ValueError) as excinfo:
        utils.binary(a)
    assert str(excinfo.value) == expected
