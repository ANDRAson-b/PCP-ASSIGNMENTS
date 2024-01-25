# Hyphenator_broken.py
# the CSC 7014
# Jan 2024
""" Inserts hyphens into a non-empty odd-length input string as follows:
A hyphen is inserted on either side of the middle character.
Example: "abcde" becomes "ab-c-de"
"""
### This program intentionally has at least one error in it!
s = input('Enter an odd-length string (remember to put quotes around it): ')
n = len(s)
m = n//2
first = s[0:m]
middle = s[m]
second = s[m+1:]
h = first+'-'+middle+'-'+second
# final output
print(s,'becomes',h)