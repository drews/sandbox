# demonstrate resilience (i.e. recovery from "disaster")

# setup some basic variables and inspect their types
number_as_string = "3"
print(type(number_as_string))
number_as_int = 3
print(type(number_as_int))

non_number_as_string = "hello world"
print(int(number_as_string)) # will work

some_number = -1 # sentinel value
try:
    # 1. have a disaster
    some_number = int(non_number_as_string) # won't work
except:
    # 2. recover from error
    print(repr(sys.exception()))
if some_number < 0:
    print("some_number is negative and thus int-parsing might've failed")