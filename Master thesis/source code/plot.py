# To plot the results

## The different datasets (ie. without noise and missing observation, with different percentage of noise,
# with different percentage of missing observations) is used to train the model.
# The results obtained are taken and plotted


import matplotlib.pyplot as plt 
import numpy as np

## To plot domain error with respect to different percentages of noise

# x axis values 
x1 = [0,10,25,50]
# corresponding y axis values 
y1 = [0,0.04,0.083,0.125]
  
# plotting the points  
plt.plot(x1, y1, color='red', linestyle='solid', linewidth = 2, 
         marker='h', markerfacecolor='red', markersize=5) 

plt.ylim(0,1) 
plt.xlim(1,50) 

plt.xlabel('Noise in %') 
plt.ylabel('Domain error') 

plt.show()

## To plot number of test problems solved by learned domain model with respect to different percentages of
# missing fluent values in observations 

# x axis values
x2 = [0,10,25,50]
# y axis values 
y2 = [28,27,27,26]
  
# plotting the points  
plt.plot(x2, y2, color='red', linestyle='solid', linewidth = 2, 
         marker='h', markerfacecolor='red', markersize=5) 

plt.ylim(0,30) 
plt.xlim(1,50) 

plt.xlabel('Missing observations in %') 
plt.ylabel('No of test problems') 
plt.show()

## To plot number of test problems solved by learned domain model with respect to different percentages of noise

# x axis values 
x3 = [0,10,25,50]
# corresponding y axis values 
y3 = [28,26,27,24]
  
# plotting the points  
plt.plot(x3, y3, color='red', linestyle='solid', linewidth = 2, 
         marker='h', markerfacecolor='red', markersize=5) 

plt.ylim(0,30) 
plt.xlim(1,50) 

plt.xlabel('Noise in %') 
plt.ylabel('No of test problems') 
  
#plt.title('My first graph!') 
plt.show()