#!/usr/bin/env python3
from flatten.exceptions import NotIntegerListException


def flatten_nested_list_integers(nested_list):
    """
    Flatten a list of integers only

    :param nested_list: required
    :type nested_list: list

    :return: flatten list

    .. code-block:: python

    Success input
        input: [1, [2, [3, [4, 5]]]]
        response: [1, 2, 3, 4, 5]

    Invalid input
        input: [1, 2, [3, [4, {5, 6}]], {7, 8, 9}, 0]
        response: None
    """
    if not isinstance(nested_list, list):
        raise NotIntegerListException

    flattened_list = list()

    for element in nested_list:
        if isinstance(element, list):
            # recursive call
            flattened_list.extend(flatten_nested_list_integers(element))
        else:
            if not isinstance(element, int):
                raise NotIntegerListException
            flattened_list.append(element)

    return flattened_list
