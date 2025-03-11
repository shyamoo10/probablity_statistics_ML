
# A certain email service uses a spam filter. Given the following probabilities:

# The probability that any random email is spam is 0.2 (20%).
# If an email is spam, the probability that it contains the word "lottery" is 0.6 (60%).
# If an email is not spam, the probability that it still contains the word "lottery" is 0.1 (10%).
# Now, suppose you receive an email that contains the word "lottery".

# Question:
# What is the probability that this email is actually spam ?


def bayes_theorem(pofa,pofbbya,pofbbya_dash):
      PofA= pofa
      PofA_dash= 1 -  pofa
      PofBByA= pofbbya
      PofBByA_dash= pofbbya_dash
      numerator= (PofA*PofBByA)
      PofB=  numerator+ (PofA_dash*PofBByA_dash)
      PofAByB=  numerator / PofB
      return  f"the result is {PofAByB*100}%"
  
  

result=  bayes_theorem(0.2,0.6,0.1) 
print(result) 

      
      
    
          
      
     
