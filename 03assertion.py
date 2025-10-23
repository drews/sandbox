# Demonstrating assertions and truth-y types in Python

# Assertion example
def divide(a, b):
    # Assert that b is not zero to avoid ZeroDivisionError
    assert b != 0, "Denominator must not be zero"
    return a / b

print("Division result:", divide(10, 2))

# Uncommenting the next line will raise an AssertionError
# print("Division result:", divide(10, 0))

# Truth-y and False-y values in Python
test_values = [None, False, 0, 0.0, '', [], {}, set(), 'hello', [1], {'a': 1}, (0,), 42]

for val in test_values:
    if val:
        print(f"{repr(val)} is truthy")
    else:
        print(f"{repr(val)} is falsey")

# Using assertion to check for truthiness
def process_data(data):
    assert data, "Data must not be empty or falsey"
    print("Processing:", data)

process_data([1, 2, 3])
# Uncommenting the next line will raise an AssertionError
# process_data([])

# Assertions are useful for debugging and enforcing invariants during development.