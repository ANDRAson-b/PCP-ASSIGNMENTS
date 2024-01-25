x=int(input('Enter x :'))
y=int(input('Enter y :'))
if(1<=x<=3 and 1<=y<=3):
    print('A')
elif(x>3):
    print('B')
elif(y<1):
    print('C')
elif(y>3):
    print('D')
else:
    print('E')

# def test(x,y):
#     if(1<=x<=3 and 1<=y<=3):
#         print('A')
#     elif(x>3):
#         print('B')
#     elif(y<1):
#         print('C')
#     elif(y>3):
#         print('D')
#     else:
#         print('E')

# a=[2,1,4,1,0,3]
# b=[2,0,1,5,3,0]
# for i in range(len(a)):
#     test(a[i],b[i])