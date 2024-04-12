def approx (x): #define the function to approximate the function for any value of x
  i=0
  a = 0.0
  error_bound = 1
  if(x<0 or x>1):
    print("Error!")
    return False
  else:
    
    while error_bound>0.0001:
     
      a += ((-1)**i*(x**(2*i+1)))/(2*i+1)
      error_bound = x**(2*i+1)/(2*i+1)
      i=i+1
      
  return (a, i, error_bound)
x = input("give me a number between 0-1  ")
x=float(x)
print(approx(x))