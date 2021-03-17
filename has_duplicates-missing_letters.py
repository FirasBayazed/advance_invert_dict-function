def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 


alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

# part 1

#Write a function called has_duplicates that takes a string parameter and returns True if 
#the string has any repeated characters. Otherwise, it should return False.

def has_duplicates(s):
    # convert all characters to lowercase, also convert numbers to string
    s = str(s).lower()  
    # as we can see if the length of our dictionary and the string not equal,
    # then the length of the string will be bigger than the length of the dictionary,
    # because we have re characters in the string, but we can't have repeated keys in the dictionary
    # so it will return True, otherwise they will have the same length and it will return False
    return len(histogram(s).keys()) != len(s)
# testing
print(has_duplicates(1))
print(has_duplicates(11))
print(has_duplicates('Alaa'))
print(has_duplicates('Firas'))   
# examples to make the code clear
print("___________with repeated characters___________")
print(has_duplicates("firaas"))
print(histogram("firaas"))
print("len of dict:",len(histogram("firaas").keys()))
print("len of str:",len("firaas"))

print("___________without repeated characters___________")
print(has_duplicates("firas"))
print(histogram("firas"))
print("len of dict:",len(histogram("firas").keys()))
print("len of str:",len("firas"))

# Write a loop over the strings in the provided test_dups list. 
# Print each string in the list and whether or not it has any duplicates
print("\ntesting:\n")
for st in test_dups:
    if has_duplicates(st):
        print(st,':',"has duplicates")
    else:
        print(st,':',"has no duplicates")

# Part 2

# Write a function called "missing_letters" that takes a string parameter and returns a new string
#  with all the letters of the alphabet that are not in the argument string.
#  The letters in the returned string should be in alphabetical order.

#import string
#string.ascii_lowercase

def missing_letters(s):
    
    alpha_list = []
    for a in alphabet:
        if a not in histogram(s).keys():
            alpha_list.append(a)
    alpha_list.sort()
    alpha_str =''.join(map(str, alpha_list))
    return alpha_str

# testing
print(missing_letters("firas"))
print()

print("'loop over the strings in list test_miss and call missing_letters'\n")



for alph in test_miss:
    # remove spaces from the string
    alph1 = alph.replace(' ','')
    # remove repeated letters
    alph1 = "".join(set(alph1))

    # sort our string an convert it to list so we can compare it with alphabet
    if sorted(alph1) != sorted(alphabet):

            print(alph,":",'is missing letters',missing_letters(alph))
    else:
            print(alph,":",'uses all the letters')

    
