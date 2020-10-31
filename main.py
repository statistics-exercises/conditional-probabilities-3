import matplotlib.pyplot as plt 
import numpy as np 

def gen_x() : 
  # Your code to generate and return the random variable X that is 
  # described in the text on the right should go here.
  

# You should not need to adjust anything from here onwards.
# This will just create the graph showing the values of the variable 
xv, yv = np.zeros(100), np.zeros(100) 
for i in range(100) : xv[i], yv[i] = i+1, gen_x() 
plt.plot( xv, yv, 'ko' )
plt.savefig( "xvals.png" )
