# This script prints all prime numbers between 1 and 100.
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)