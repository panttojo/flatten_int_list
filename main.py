from flatten.exceptions import NotIntegerListException
from flatten.lib import flatten_nested_list_integers


nested_integers_list = [1, [2, [3, [4, 5]]]]
flattened_list = flatten_nested_list_integers(nested_integers_list)

inval_list = [5000, "a", "b", [{"c", "d"}, [1, 2, [3, [4, [5]]]]]]

try:
    print("-------------------------------------------------")
    print("input list of integers: {}".format(nested_integers_list))
    print("flattened list: {}".format(flattened_list))
    print("-------------------------------------------------")
    print("Response for the next list: {}".format(inval_list))
    flatten_nested_list_integers(inval_list)
except NotIntegerListException as exc:
    print(exc.message)

print("-------------------------------------------------")
print("Development by Daniel Pantoja (:")
print("-------------------------------------------------")
