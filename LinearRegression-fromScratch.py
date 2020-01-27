#!/usr/bin/env python
# coding: utf-8

# In[103]:


from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import random


# # beginning with small sample dataset

# In[105]:


# xs = np.array([1,2,3,4,5,6], dtype = np.float64)
# ys = np.array([5,4,6,5,6,7], dtype = np.float64)

# plt.scatter(xs, ys)
# plt.show()


# In[106]:


# m =[ x'.y' - (xy)'] / [ (x')^2 - (x^2)']


# In[107]:


def best_fit_slope_int(xs, ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys))/
        ((mean(xs)**2)- mean(xs**2)))
    b = mean(ys) - m*mean(xs)        
    return m,b


# In[108]:


m,b = best_fit_slope_int(xs, ys)


# In[109]:


m #best fit slope


# In[110]:


b #best fit line


# In[111]:


regression_line = [m*x + b for x in xs]


# In[91]:


# two plots one scatter for the points and
#one line for the regression line y predicted points
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()


# In[93]:


predict_x = 8
predict_y = m*predict_x + b


# In[94]:


plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color = 'red')
plt.plot(xs, regression_line)
plt.show()


# # R**2

# Calculating r**2 ie coefficient of determination.
# It is the value of how good of a fit is our best fit line

# In[83]:


def squared_error(ys_orig, ys_line):
    return sum((ys_orig - ys_line)**2)


# In[84]:


def coefficientOfDetermination(ys_orig,ys_line):
    y_mean_line= [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr/ squared_error_y_mean)


# In[96]:


r_squared = coefficientOfDetermination(ys, regression_line )
r_squared


# # Testing

# In[56]:


def create_dataset(hm, variance, step=2, correlation= False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64),np.array(ys, dtype=np.float64) 


# In[71]:


xs, ys = create_dataset(40, 80, 2, correlation = False)


# In[101]:


xs, ys = create_dataset(40, 40, 2, correlation = 'pos')
m,b = best_fit_slope_int(xs, ys)

print(m)#best fit slope

print(b) #best fit line

regression_line = [m*x + b for x in xs]

# two plots one scatter for the points and
#one line for the regression line y predicted points
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()
r_squared = coefficientOfDetermination(ys, regression_line )
r_squared


# In[99]:


xs, ys = create_dataset(40, 10, 2, correlation = 'pos')
m,b = best_fit_slope_int(xs, ys)

print(m)#best fit slope

print(b) #best fit line

regression_line = [m*x + b for x in xs]

# two plots one scatter for the points and
#one line for the regression line y predicted points
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()
r_squared = coefficientOfDetermination(ys, regression_line )
r_squared


# In[100]:


xs, ys = create_dataset(40, 80, 2, correlation = 'pos')
m,b = best_fit_slope_int(xs, ys)

print(m)#best fit slope

print(b) #best fit line

regression_line = [m*x + b for x in xs]

# two plots one scatter for the points and
#one line for the regression line y predicted points
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()
r_squared = coefficientOfDetermination(ys, regression_line )
r_squared

