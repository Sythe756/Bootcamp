num = int(input("Please enter a number: "))
for z in range(1,13):
  x = z * num
  print(num , "x" ,  z, "=" , x)
#or
a = int(input("please enter a number: "))
for y in range(1,13):
  z = y * x
  print('{} x {} = {}'.format(x,y,z))
