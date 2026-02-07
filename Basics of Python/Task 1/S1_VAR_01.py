an_int = 10
a_float = 3.14
a_str = "hello"
a_bool = True
a_none = None
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
a_dict = {"a": 1}
a_set = {1, 2, 3}
a_function = lambda x: x * 2

values = [
    ("an_int", an_int),
    ("a_float", a_float),
    ("a_str", a_str),
    ("a_bool", a_bool),
    ("a_none", a_none),
    ("a_list", a_list),
    ("a_tuple", a_tuple),
    ("a_dict", a_dict),
    ("a_set", a_set),
    ("a_function", a_function),
]

print(f"{'name':<12} {'value':<20} {'type(x)':<25} {'type(x).__name__'}")
print("-" * 80)
for name, value in values:
    print(f"{name:<12} {str(value):<20} {str(type(value)):<25} {type(value).__name__}")
