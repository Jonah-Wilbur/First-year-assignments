import numpy as np
def f(x):
  return x**2
def g(x):
  return np.sin(x)
def h(x):
  return np.exp(x)
def differentiate(f,c,e): #define function
  d = 10**-8 #define step size
  m = (f(c+d)-f(c-d))/(2*d)  #define slope using step size and c
  x1 = c
  x2 = c
  error1 = abs(f(x1)-f(c)-(x1-c)*m) #define error
  error2 = abs(f(x2)-f(c)-(x2-c)*m) #define error again
  while error1<e:
    x1=x1-0.000001
    error1 = abs(f(x1)-f(c)-(x1-c)*m) #this will find the error of the linear approximation at each step
    if(error1>=e): #if the error is too great, stop
      print(x1)
      break
  while error2<e:
    x2=x2+0.000001
    error2 = abs(f(x2)-f(c)-(x2-c)*m) #this will find the error of the linear approximation at each step
    if error2>=e: #if the error is too great, stop
      print(x2)
      break
      

differentiate(f,1,0.1)
differentiate(g,np.pi/4,0.05)
differentiate(h,0,0.01)