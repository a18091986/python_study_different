a = [1,2,3,4]
b = (-1,3,5,7)
print(b[1], type(b))
c = zip(a,b)
for item in c.__iter__():
    print(item)


