# Task: String Reversal

# Create a Python function that takes a
# string as input and returns the reverse of
# that string. For example, if the input is
# "hello,

# " the function should return

# "olleh.
# "

# here i mentioned different different functions which can be used to reverse of the string hello

def reverse_using_slicing(s):
    return s[::-1]

def reverse_using_join(s):
    return ''.join(reversed(s))

def reverse_using_loop(s):
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

def reverse_using_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_using_recursion(s[1:]) + s[0]

input_string = "hello"

reversed_slicing = reverse_using_slicing(input_string)
reversed_join = reverse_using_join(input_string)
reversed_loop = reverse_using_loop(input_string)
reversed_recursion = reverse_using_recursion(input_string)

print("reverse_using_slicing:",reversed_slicing)    # Output: olleh
print("reverse_using_join:",reversed_join)       # Output: olleh
print("reverse_using_loop:",reversed_loop)       # Output: olleh
print("reverse_using_recursion:",reversed_recursion)  # Output: olleh
