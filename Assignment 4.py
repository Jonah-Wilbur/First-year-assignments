import matplotlib.pyplot as plt #import libraries
import numpy as np
def f(x):
      return x**2 #define functions for the assignment
def g(x):
    return -3*(x**3)+10*(x**2)-5*x-3
def funny_function(x):
    if x>0:
        return x**x
    elif x==0:
        return 1
    else:
        return abs(x)**abs(x)
def deriv(f, base):
      return ((f(base+10**(-5))-f(base))/(10**(-5)))
#difference between very small step to the left and very small step to the right
def gradient_descent(f, L, x0):
    x_coords = []
    y_coords = []
    x_coords.append(x0) #set the first x coordinate to be x0
    y_coords.append(f(x0)) #set the first y coordinate to be f(x0)
    xi=x0
    i=1
    while abs(deriv(f,xi))>0.01:
        xi=x_coords[i-1]-L*deriv(f,x_coords[i-1])
        #x1 is x0 + learning_value * f'(x) at this point
        yi=f(xi)
        x_coords.append(xi) #add xi to x as the last falue
        y_coords.append(yi) #add yi to y as the last value
        i=i+1



    plot_range = np.linspace(min(x_coords)-0.5,max(x_coords)+0.5,1000)
    f_range = [f(i) for i in plot_range]
    plt.plot(plot_range,f_range) #plot the range and function
    plt.plot(x_coords,y_coords) #plot the x and y coords of Euler's method
    plt.show()
    print(x_coords[i-1])

gradient_descent(f,0.9,5)
