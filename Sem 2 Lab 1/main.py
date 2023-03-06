# ScriptName: main.py
# Author: <add your name here>

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()

print(firsts("He fell off"))

# print(iter_factorial(8))

# print(removeVowels("Lemme get dat shit"))

# print(chooseLargest([1,2,3,4,5],[2,2,9,0,9]))

# print(loop_the_loop("Woah","Wee"))

print(hailstone(80))

# print(chooseLargest([1,2,3,4,5],[2,2,9,0,9]))

print(loop_the_loop("Woah","Wee"))

print(F("Poop", "Pee"))



# name = "Harry"

# print(len(name))
    
# print(F("Whassup", "What"))