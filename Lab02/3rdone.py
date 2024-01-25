x = 1
y = 5
z = 10
a=[x<z,
2*y>=z,
2*y<z,
(x>1) or(z!=7),
y!=(z/2),
(x>0)or((y>0)or(z<0)),
((x>0)or(y>0))or(z<0)]
print(a)

x = 'Cornell'
y = 'Harvard'
z = 'Yale'
a=[x!=z,
x=='cornell',
len(x)>len(y),
y[1:]>z[1:],
len(x+z)>len(y)]
print(a)
print(y[1:]>z[1:])