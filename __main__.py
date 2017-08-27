from observable_primitives import ObservableInteger, ObservableFloat, ObservableComplex, ObservableBool
from observable_primitives.observers.debug_observers import HoldNumericPrintObserver

obs_int = ObservableInteger(2)
obs_float = ObservableFloat(2)
obs_complex = ObservableComplex(complex(1, 1))
obs_bool = ObservableBool(True)

# Observer
observer = HoldNumericPrintObserver([obs_int, obs_float, obs_complex, obs_bool])

# Binary operators
binary = [
    "+", "-", "*", "@", "/", "//", "%", "**", "<<", ">>", "&", "^", "|"
]
binary_functions = [
    "divmod", "pow",
]

# Unary operators
unary = [
    "-", "+", "abs", "~", "complex", "int", "float", "round", "str", "repr", "bytes", "hash",
]

# Augmented operators
augmented = [
    "+=", "-=", "*=", "@=", "/=", "//=", "%=", "**=", "<<=", ">>=", "&=", "^=", "|="
]

# Class tests
variables = [obs_int, obs_float, obs_complex, obs_bool]
variable_names = ["obs_int", "obs_float", "obs_complex", "obs_bool"]
classes_names = ["ObservableInteger", "ObservableFloat", "ObservableComplex", "ObservableBool"]

# Go through tests
for obj_name, obj, class_name in zip(variable_names, variables, classes_names):
    print(f"\nTesting: {class_name}")

    # BINARY OPERATORS
    test_number = 2
    for operator in binary:
        try:
            eval_string = f"{obj_name} {operator} {test_number}"
            a = eval(eval_string)
            print(f"\t{obj_name}: {eval(obj_name)} {operator} {test_number} = {a}")
        except TypeError:
            print(f"\t{obj_name}: {eval(obj_name)} {operator} {test_number} = UNSUCCESSFUL")

    # BINARY FUNCTIONS
    print("")
    test_number = 2
    for operator in binary_functions:
        try:
            eval_string = f"{operator}({obj_name}, {test_number})"
            a = eval(eval_string)
            print(f"\t{obj_name}: {operator}({eval(obj_name)}, {test_number}) = {a}")
        except TypeError:
            print(f"\t{obj_name}: {operator}({eval(obj_name)}, {test_number}) = UNSUCCESSFUL")

    # UNARY OPERATORS
    print("")
    for operator in unary:
        try:
            eval_string = f"{operator}({obj_name})"
            a = eval(eval_string)
            print(f"\t{obj_name}: {operator}({eval(obj_name)}) = {a}")
        except TypeError:
            print(f"\t{obj_name}: {operator}({eval(obj_name)}) = UNSUCCESSFUL")

    # AUGMENTED OPERATORS
    test_number = 2
    print("")
    try:
        obj += test_number
        print(f"\tobj += {test_number}: Success")
    except TypeError:
        print(f"\tobj += {test_number}: UNSUCCESSFUL")
    try:
        obj -= test_number
        print(f"\tobj -= {test_number}: Success")
    except TypeError:
        print(f"\tobj -= {test_number}: UNSUCCESSFUL")
    try:
        obj *= test_number
        print(f"\tobj *= {test_number}: Success")
    except TypeError:
        print(f"\tobj *= {test_number}: UNSUCCESSFUL")
    try:
        obj @= test_number
        print(f"\tobj @= {test_number}: Success")
    except TypeError:
        print(f"\tobj @= {test_number}: UNSUCCESSFUL")
    try:
        obj /= test_number
        print(f"\tobj /= {test_number}: Success")
    except TypeError:
        print(f"\tobj /= {test_number}: UNSUCCESSFUL")
    try:
        obj //= test_number
        print(f"\tobj //= {test_number}: Success")
    except TypeError:
        print(f"\tobj //= {test_number}: UNSUCCESSFUL")
    try:
        obj %= test_number
        print(f"\tobj %= {test_number}: Success")
    except TypeError:
        print(f"\tobj %= {test_number}: UNSUCCESSFUL")
    try:
        obj **= test_number
        print(f"\tobj **= {test_number}: Success")
    except TypeError:
        print(f"\tobj **= {test_number}: UNSUCCESSFUL")
    try:
        obj <<= test_number
        print(f"\tobj <<= {test_number}: Success")
    except TypeError:
        print(f"\tobj <<= {test_number}: UNSUCCESSFUL")
    try:
        obj >>= test_number
        print(f"\tobj >>= {test_number}: Success")
    except TypeError:
        print(f"\tobj >>= {test_number}: UNSUCCESSFUL")
    try:
        obj &= test_number
        print(f"\tobj &= {test_number}: Success")
    except TypeError:
        print(f"\tobj &= {test_number}: UNSUCCESSFUL")
    try:
        obj ^= test_number
        print(f"\tobj ^= {test_number}: Success")
    except TypeError:
        print(f"\tobj ^= {test_number}: UNSUCCESSFUL")
    try:
        obj |= test_number
        print(f"\tobj |= {test_number}: Success")
    except TypeError:
        print(f"\tobj |= {test_number}: UNSUCCESSFUL")

    print("")
    print("\tObserver observed the following updates:")
    observer.print(indent=8)
