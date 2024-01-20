#Declaration of variables
arr=[0,0,0,0] #List

#giving instructions for user about input and scanning it
#Integer
cents=int(input("Change Maker \n Enter amount of change to make (1 to 99 cents):"))

#Displaying conformation for entered input 
print("\n\nTo make change for",cents,"cents  ")

#proces to split cents
while(cents>0):
    if(cents>=25):
        arr[0]=cents//25;
        cents%=25;
    elif(cents>=10):
        arr[1]=cents//10;
        cents%=10;
    elif(cents>=5):
        arr[2]=cents//5;
        cents%=5;
    else:
        arr[3]=cents;
        cents%=1;

#Displaying split cents in quarters, dimes, nickels, and pennies
print("",arr[0],"quarter\n",arr[1],"dimes\n",arr[2],"nickels\n",arr[3],"pennies\n")