# Hyphenator_even.py
# the CSC 7014
# Jan 2024
""" Inserts hyphens into a non-empty even-length input string as follows:
The hyphen splits the first and second halves.
"""
## We've added a number of so-called "debugging" print statements here
s = input('Enter an even-length string (remember to put quotes around it): ')
n = len(s)
print('n is',n)
if n%2 == 0: # Line A
    # s has even length
    m = n//2
    print('even case. m is',m)
    first = s[0:m-1] # Line B
    print('even case. first is',first)
    second = s[m+1:] # Line C
    print('even case. second is',second)
    h = first + '-' + second
# final output
print(s,'becomes',h)