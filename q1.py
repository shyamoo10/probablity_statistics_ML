data = [12, 15, 14, 10, 18, 20, 22, 24, 19, 17]
# 1️⃣ Write a function to calculate the mean (average).
# 2️⃣ Write a function to calculate the variance.
# 3️⃣ Write a function to calculate the standard deviation.

def main():
   
  def calc_mean(numbers):
     sum=0
     for  number in numbers:
         sum+=number
     
     mean=  sum/len(numbers)
     return mean
 
  def calc_variance(numbers):
       sum=0
       mean= mean_rslt
       for number in numbers:
           value= (number - mean)**2
           sum+=value
       variance= sum/len(numbers)
       return variance
  def calc_SD():
       variance= variance_rslt
       SD= variance**(1/2)
       return SD
      
           
  mean_rslt=  calc_mean(data) 
  variance_rslt=  calc_variance(data)
  sd_rslt= calc_SD()
  
  
  print(f"mean : {mean_rslt}")
  print(f"variance :{variance_rslt}")
  print(f"SD :{sd_rslt}")
  
  
   
    
main()    
    