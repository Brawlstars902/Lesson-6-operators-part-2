a=input('Please enter a number.\n')
b=input('please enter a second number.\n')
c=input('Please enter a third number.\n')
if a!=b!=c:
    print('None of the numbers are equal to each other.\n')
elif a== b!= c:
    print(a,'is equevalent to',b,'but differs from',c,'.')
elif b==c!=a:
    print(b,'is equevalent to',c,'but differs from',a,'.')
elif a==c !=b:
    print(a,'is equevalent to',c,'but differs from',b,'.')
else:
    print('All the numbers are equal.')