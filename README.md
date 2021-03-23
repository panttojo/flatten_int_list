# flatten list of integers

# run tests
```
pytest flatten/tests.py 
```
Flatten a list of integers only
```
:param nested_list: required
:type nested_list: list
:return: flatten list

    Success input
        input: [1, [2, [3, [4, 5]]]]
        response: [1, 2, 3, 4, 5]

    Invalid input
        input: [1, 2, [3, [4, {5, 6}]], {7, 8, 9}, 0]
        response: NotIntegerListException
```
