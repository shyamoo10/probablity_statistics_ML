from q1 import *

data = [50, 52, 53, 49, 100, 48, 47, 51, 49, 50, 500]

# 1️⃣ Find the mean and standard deviation.
# 2️⃣ Identify numbers that are more than 3 standard deviations away from the mean (outliers).


mean=  calc_mean(data)
variance=  calc_variance(mean,data)
sd=   calc_SD(variance)
outliers=  []


for number in data:
    if number > (sd*3):
        outliers.append(number)

print(f"mean : {mean}")
print(f"sd :  {sd}")
print(f"outliers : {outliers}")