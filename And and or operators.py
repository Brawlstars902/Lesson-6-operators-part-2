a=int(input('Please enter a number to find the positive or negative value.\n'))
b=int(input('Please enter another number to find the positive or negative value.\n'))
c=int(input('Please enter another number to find the positive or negative value.\n'))
if a or b or c>0:
    print('One of the numbers are greater than 0 meaning they are positive.')
elif a or b or c<0:
    print('One of the numbers are less than 0 meaning they are negative numbers.')
else:
    print('All the numbers are 0, meaning that they are neither positive nor negative.')