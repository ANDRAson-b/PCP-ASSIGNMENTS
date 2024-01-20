#importing math package
import math

#Declering litrealas and assigning them with instructions
diameter=int(input("Pizza Pricer\n Enter diametermeter of pizza (inches): ")) #integer
dollers=float(input("Enter cost of pizza (dollars) : ")) # float

#process to compute the conditions
#converting dollers to cents
cents=int(dollers*100) #Integer 

#calculating area
area=math.pi*diameter*diameter*0.25 # float

#calculating how many people can eat pizza 
people=int(area/50) #Integer

#calculating cost in cents
centsPerSquareInch=cents/area #float

#calculting dollers need to pay accordingly with tip
cost=dollers/people #float
tip=(15*cost)/100 #float
costPerPerson=cost+tip #float

#Displaying the reqested output
print("\n This pizza",people,
    "people\n  cents/square inch\t =",centsPerSquareInch,
    "\n  cost/person\t =",costPerPerson,"dollers (includes a 15% tip)")