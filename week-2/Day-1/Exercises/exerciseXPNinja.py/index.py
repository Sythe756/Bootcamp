#EX 3
# 3 <= 3 < 9

a = 3 <= 3 < 9
print(a)
#true


#>>> 3 == 3 == 3
b = 3 == 3 == 3
print(b)
#true


#>>> bool(0)
c = bool(0)
print(c)
#false


#>>> bool(5 == "5")
d = bool(5 == "5")
print(d)
#false


#>>> bool(4 == 4) == bool("4" == "4")
e = bool(4 == 4) == bool("4" == "4")
print(e)
#true


#>>> bool(bool(None))
f = bool(bool(None))
print(f)
#false


x = (1 == True)
y = (1 == False)
i = True + 4
j = False + 10
print("x is", x)
print("y is", y)
print("i:", i)
print("j:", j)

#x is True . .... . because 1 == True
#y is False . .... . because 1 isnt ==  True but 0 == False
#i: 5 . ... . because True == 1 so 1 + 4 = 5
#j: 10 . ... . because False == 0 so 0 + 10 = 10
