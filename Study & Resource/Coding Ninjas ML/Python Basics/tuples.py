t = (1,2,3)
print(type(t))
print(t[0])

t = (1, "23dd", 2, True)
print(t)

#tuples are immutable
# t[0] = 23    #INVALID
print(t[0:2])   #slicing

#operators
t = (1,2)
k = ("d", 1)
print(t+k)
#print(t*k)  #error
print(t*2)
print(1 in t)
print("d" in t)
