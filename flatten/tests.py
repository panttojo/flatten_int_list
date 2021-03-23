import pytest

from flatten.exceptions import NotIntegerListException
from flatten.lib import flatten_nested_list_integers


def test_flatten_empty_list():
    empty_list = []
    assert flatten_nested_list_integers(empty_list) == empty_list


def test_flatten_nested_integer_list():
    nested_list = [1, [2, [3, [4, [5]]]]]
    expected_flatten_list = [1, 2, 3, 4, 5]
    assert flatten_nested_list_integers(nested_list) == expected_flatten_list


def test_flatten_no_nested_list():
    simplet_list = [1, 2, 3, 4, 5]
    assert flatten_nested_list_integers(simplet_list) == simplet_list


def test_invalid_input_list():
    invalid_list = [5000, "a", "b", [{"c", "d"}, [1, 2, [3, [4, [5]]]]]]

    with pytest.raises(NotIntegerListException) as exc:
        flatten_nested_list_integers(invalid_list)

    assert exc.value.message == NotIntegerListException.message
