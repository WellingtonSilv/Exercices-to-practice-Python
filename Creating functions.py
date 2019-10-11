#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#function to calculate the len of a list
def length(x):
    leng=0
    for i in x:
        leng=leng+1
    return(leng)


# In[ ]:


#creating a function to calculate the max value of a list of values
def max(x):
    for i in x:
        m=i
        for j in x:
            if m<j:
                m=j
    return(m)
    


# In[ ]:


#creating a function to calculate the min value of a list of values
def min(x):
    for i in x:
        m=i
        for j in x:
            if m>j:
                m=j
    return(m)
    


# In[ ]:


#creating a function to calculate the sum of a list of values
def sum(x):
    suma=0
    for i in x:
        suma=suma+i
    return(suma)


# In[ ]:


#creating a function to calculate the mean of a list of values
def mean(x):
    m=0
    suma=0
    for i in x:
        suma=suma+i
        m=m+1
    return(suma/m)


# In[ ]:


#creating a function to calcule the the squart root of a number
def sqrt(x):
    sq=x**0.5
    return(sq)


# In[ ]:


#creating a function to calculate the standart deviation of a list of values
def sd(x):
    #fiding the mean of the list
    m=0
    suma=0
    for i in x:
        suma=suma+i
        m=m+1
    meaan=suma/m
    #find the distance from each data point to 
    #the mean and square each of those distances and sum this values into sq_dst
    sq_dst=0
    for i in x:
        dst=i-meaan
        sq_dst=sq_dst+(dst**2)
    #counting the number of elements in list
    leng=0
    for i in x:
        leng=leng+1
    #dividing sq_dst by leng
    almost_sd = sq_dst/leng
    #fiding standart deviation
    stand_devi=almost_sd**0.5
    return(stand_devi)


# In[ ]:


#write a a function that return a summary with the follow informations:
#the len of the list, the max value, the min value,the sum, the mean and the standart deviation

def list_info(x):
    #calculating the len
    leng=0
    for i in x:
        leng=leng+1
        
    #calculating the sum
    suma=0
    for i in x:
        suma=suma+i
        
    #calculating the max
    for i in x:
        m=i
        for j in x:
            if m<j:
                m=j
                
    #calculating the min
    for i in x:
        mi=i
        for j in x:
            if mi>j:
                mi=j
                
    #calculating the mean
    ma=0
    sm=0
    for i in x:
        sm=sm+i
        ma=ma+1
    meaan=sm/ma
    
    #caltulating standart deviation
    y=0
    su=0
    for i in x:
        su=su+i
        y=y+1
    man=su/y
    sq_dst=0
    for i in x:
        dst=i-man
        sq_dst=sq_dst+(dst**2)
    leg=0
    for i in x:
        leg=leg+1
    almost_sd = sq_dst/leg
    stand_devi=almost_sd**0.5
    
    #returning results
    return(print("#------Summary------#"),
           print(),
           print("The length is:",leng,""),
           print(),
           print("The sum is:",suma,""),
           print(),
           print("The max value is:",m,""),
           print(),
           print("The min value is:",mi,""),
           print(),
           print("The mean is:",meaan,""),
           print(),
           print("The standart deviation is:",stand_devi,""))
    


# In[ ]:




