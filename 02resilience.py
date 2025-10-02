# demonstrate resilience (i.e. recovery from "disaster")
import sys

# setup some basic variables and inspect their types

a = "3"
print(type(a)) # <type str>
print(int(a)) # will work

b = 3
print(type(b))

c = "hello world"

some_number = -1 # sentinel value
try:
    # 1. have a disaster
    some_number = int(c) # won't work
except:
    # 2. recover from error
    print(repr(sys.exception()))
if some_number < 0:
    print("some_number is negative and thus int-parsing might've failed")

