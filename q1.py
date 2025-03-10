data = [12, 15, 14, 10, 18, 20, 22, 24, 19, 17]
# 1️⃣ Write a function to calculate the mean (average).
# 2️⃣ Write a function to calculate the variance.
# 3️⃣ Write a function to calculate the standard deviation.


   
def calc_mean(numbers):
     sum=0
     for  number in numbers:
         sum+=number
     
     mean=  sum/len(numbers)
     
     
     return mean
 
def calc_variance(mean,numbers):
       sum=0
       
       for number in numbers:
           value= (number - mean)**2
           
           sum+=value
           
       variance= sum/len(numbers)
       
       return variance
   
   
def calc_SD(variance):
       
       SD= variance**0.5
     
       return SD
      
           



  
  



  
  
   
    
 
    