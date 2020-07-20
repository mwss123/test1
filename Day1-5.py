

num1 = int(input('Number :'))

if num1 % 3 == 0 and num1 % 7 == 0 :
    print('{0} = 3 X [ ] = 7 X [ ]'.format(num1))

elif num1 % 3 == 0 :
    print('3 X [ ] = {0}'.format(num1))

elif num1 % 7 == 0 :
    print('7 X [ ] = {0}'.format(num2))

else : 
    print('Noooo') 
