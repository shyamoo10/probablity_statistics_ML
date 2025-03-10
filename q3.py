# 1️⃣ Write a function to simulate flipping a coin (Heads or Tails).
# 2️⃣ Run this function 1000 times and count how many times you get Heads vs. Tails.
# 3️⃣ Calculate the probability of getting Heads.

import random
 
def flip_coin():
 rand=  random.randrange(0,2) 
 if rand==0:
     return "Head"
 else:
     return "Tail"
 
 
def flipping_thousand():
    H_count= 0
    T_count=0
    for i in range(1,1001):
        result= flip_coin()
        if result=="Head":
            H_count+=1
        elif result=="Tail":
            T_count+=1
    return H_count,T_count


def prob_of_getting_Head():
       head_count,tail_count= flipping_thousand()      
       prob=  head_count/1000
       return prob
   

flip_coin()
flipping_thousand()
prob=  prob_of_getting_Head()
print(f"probability of getting head : {prob}")   
     
 
     