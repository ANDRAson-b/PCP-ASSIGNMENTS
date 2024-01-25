# FormatPlay.py
# the CSC 7014
# Jan 2024
""" A short script that illustrates formatted print."""
from math import pi
x = 355
y = 113
z = float(x)/float(y)
err = abs(z - pi)
print ('\nNumerator Denominator Quotient Error')
print ('-----------------------------------------------')
print('%3d %3d %9.7f %1.2e' % (x,y,z,err))
