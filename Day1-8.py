
num = int(input('Number :'))

while num>0 :
    fac = 1

    for i in range(1, num+1) :
        fac *= i

    print(fac)
    break  



"""
# Teacher

while num > 0 :
    result *= num
    num -= 1

print(result)
"""  
