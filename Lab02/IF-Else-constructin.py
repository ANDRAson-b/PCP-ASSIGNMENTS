# s='apples'
# if(s[-2:].endswith('ss')):
#     print('Plural')
# else:
#     print('Not Plural')

s='1246'
if(len(s)%2==0):
    print(3*int(s[-2:]))
else:
    print(7*int(s[len(s)//2]))