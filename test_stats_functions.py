import pytest

from stats_functions import (
    find_maximum,
    find_mean,
    find_median,
    find_median_absolute_deviation,
    find_minimum,
    find_standard_deviation,
    find_variance,
    sort_list,
)

# Yeh wahi grades hain jo aapke project mein hain
GRADES = [8, 6, 1, 7, 8, 9, 8, 7, 10, 7, 6, 9, 7]


def test_minimum():
    assert find_minimum(GRADES) == 1


def test_maximum():
    assert find_maximum(GRADES) == 10


def test_mean():
    assert find_mean([2, 4, 6]) == 4


def test_variance():
    assert find_variance([2, 4, 6]) == 2.67


def test_standard_deviation():
    assert find_standard_deviation(GRADES) == 2.11


def test_median_odd_length():
    assert find_median([3, 1, 2]) == 2


def test_median_even_length():
    assert find_median([4, 1, 3, 2]) == 2.5


def test_mad():
    assert find_median_absolute_deviation(GRADES) == 1


def test_sort_list():
    assert sort_list([3, 1, 2]) == [1, 2, 3]


def test_sort_does_not_change_original():
    original = [3, 1, 2]
    sort_list(original)
    assert original == [3, 1, 2]


def test_empty_list_gives_error():
    with pytest.raises(ValueError):
        find_mean([])
