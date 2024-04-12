import math

def f(x):
  if x == 0:
    x = x + 0.00000000000001
  return (math.e**x + math.log(x)) #defining functions as per the question
def g(x):
  return (math.atan(x) - x**2)
def h(x):
  return math.sin(x) / math.log(x)
def i(x):
  return math.log(math.cos(x))

def IVT(f, a, b):
  dif = 1
  x = 1
  if f(a)*f(b)>0: #if the product of two points of a function is greater than 0, there are no roots in that interval
    print("interval has no roots")
  if f(a) == 0:
    return a
  if f(b) == 0:
    return b
  while dif > 0.000000000001:
    x = (a + b) / 2
    if (f(a) * f(x)) < 0:
      b = x #move the point towards a, until you hit the root
      dif = abs(b - a) #redefine the difference
    elif (f(x) * f(b)) < 0:
      a = x #move the point towards b, until you hit the root
      dif = abs(b - a)
  return round(((a + b) / 2), 10) #return the point of the root, rounded to 10 decimal places


print(IVT(f, 0, 1)) #print statements for the assignment
print(IVT(g, 0, 2))
print(IVT(h, 3, 4))
print(IVT(i, 5, 7))
