# ScriptName: my_functions.py
# Author: Peter Lucey 118502179

# template for calling functions in another file

def print_function():
    print("I'm in another file :)")

#1.
def firsts(word:str):
    '''Return a string containing the first occurence of each character in the input'''
    try:
        #an empty string into which the new version of the word can be placed.
        new_string:str = ""
        #a list into which the characters of word can be moved.
        letters:list = []
        #saving the length of the word to a unique variable.
        length:int = len(word)
        #loop a number of times equal to zero to the length of the word.
        for num in range(length):
            #add the character at the index of the word as specified by num to the letters list.
            letters.append(word[num])
        #create a new empty list.
        s:list = []
        #loop through the contents of letters and add any element that is in letters but not in s to s.
        for i in letters:
            if i not in s:
                s.append(i)
        #move the elements of s to the new string and return it.
        for i in s:
            new_string += i
        return new_string
    #error handling.
    except:
        return "Oops"
#2.
def F(s1:str, s2:str):
    '''Places the values that are in both parameters into a list and returns that list'''
    try:
        #a list to place the common elements of both s1 and s2 into.
        result:list = []
        #a counter.
        countup1:int = 0
        #while the counter is not equal to the length of s1 add the character of s1 at the index of the counter to the empty list if it is also in s2.
        while countup1 != len(s1):
            if s1[countup1] in s2:
                result.append(s1[countup1])
                #increment the counter
                countup1 += 1
            else:
                #if the characters are not shared between s1 and s2 just increment the counter.
                countup1 += 1
        #return the common characters between s1 and s2.
        return result
    #error handling.
    except:
        return "Oops"
#3.        
def iter_factorial(n:int):
    '''Return the factorial of a given integer'''
    try:
        #set the factorial
        factorial:int = 1
        for num in range(1,n + 1):
            #multiply the factorial by each number in the range and save it to the factorial
            factorial = factorial*num
        return factorial
    #error handling.
    except:
        return "Oops"

#4.
def removeVowels(sentence:str):
    '''Takes the vowels out of the parameter and places the remaining characters in a list before returning that list as a string'''
    try:
        #a list of vowels so that 'sentence' can be compared against them to see if it contains any of them.
        vowels:list = ["a", "e", "i", "o", "u"] 
        #an empty list to place our new, vowel-less sentence into.
        no_vowel_list:list = []
        #a counter to increment.
        zeb:int = 0
        #the while loop will persist as long as the counter is less than the length of the sentence.
        while zeb != len(sentence):
            #if the character at the index that the counter indicates is not a vowel then it will be added to no_vowel_list.
            if sentence[zeb] not in vowels:
                no_vowel_list.append(sentence[zeb])
                #increment the counter.
                zeb += 1
            #if the character at the index that the counter indicates is a vowel then it will not be added to no_vowel_list.
            elif sentence[zeb] in vowels:
                #increment the counter.
                zeb += 1
        #return the contents of no vowel list as a string.
        return ''.join (no_vowel_list)
    #error handling.
    except:
        return "Oops"
#5.
def hailstone(n:int):
    '''Returns the hailstone sequence of positive integer "n" '''
    try:
        #n is placed into hailstone_list
        hailstone_list:list = [n]
            #this while loop should continue until n converges at 1
        while n > 1: 
                #if n is odd then add 1 to it and multiply it by 3 before assigning this value to n
                    if n % 2 != 0:
                        hailstone_list += [3*n+1]
                        n = 3*n+1
                        continue
                #if n is even then use integer division to divide it by 2 and add that to hailstone_list and assign n to it
                    elif n % 2 == 0:
                        hailstone_list += [n//2]
                        n = n//2
                        continue
            #return final list 
        return hailstone_list
    #error handling
    except:
        return "Oops"

#6.
def chooseLargest(a:list,b:list): 
    '''Compares the values of two different lists and moves the largest ones to another list which is then returned'''
    i:int = 0 #create a counter beginning at 0
    try:
        #create an empty list
        biggest:list = []
        #while the counter is less than the length of list 'a', loop through the list
        while i < len(a):
            #if the element at list 'a' is larger than the element at the same position of list 'b' then append the element in 'a' to the 'biggest' list
            if a[i] > b[i]:
                biggest.append(a[i])
            else:
                #if the element at list 'b' is larger than the element at the same position of list 'a' then append the element in 'b' to the 'biggest' list
                biggest.append(b[i])
            #increment the counter by 1
            i += 1
        #return a new list containing the largest values
        return biggest
    #error handling
    except:
        return "Oops"

#7.
def loop_the_loop(a1:list, a2:list): 
    '''Adds each element in a1 to each element in a2 and moves these pairings into a list which is then returned'''
    #an empty list.
    loop_list:list = []
    #a counter.
    i:int = 0 
    try:
        #create nested while loop and a new counter for a2.
        while i < len(a1):
            i2:int = 0
            while i2 < len(a2):
                #add each element in a1 to each element in a2 and add each individual pairing to loop_list. After each addition, increment the counters by 1.
                loop_list.append(a1[i]+a2[i2])
                i2 += 1
            i += 1
        #return a list of each element in a1 added to each element in a2.
        return loop_list
    #error handling.
    except:
        return "Oops"

