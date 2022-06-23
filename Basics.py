# Write a program to print your name.

print ("MOHD TALIB")

# Write a program for a Single line comment and multi-line comments.
#In PYTHON, we use the hash symbol (#) to write a single-line comment
"""
This
is
multiline
comment
"""
print("Multi-line commenting")

# Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

a = 4
print("Type of a: ", type
(a))
b = True
print("Type of b: ", type
(b))
c = 5.78
print("Type of c: ", type
(c))
d = 'Hello'
print("Type of c: ", type(d))
e = 5 + 4j
print("Type of e",type(e))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

i = 4
# Uses global because there is no local 'i'
def f():
    print('Inside f() : ', i)
# Variable 'i' is redefined as a local
def g():
    i = 2
    print('Inside g() : ', i)
# Uses global keyword to modify global 'i'
def h():
    global i
    i = 4      #Value of 'i' modified
    print('Inside h() : ', i)
# Global scope
print('global : ', i)
f()
print('global : ', i)
g()
print('global : ', i)
h()
print('global : ', i)
