print('IT IS SIMPLE CALCULATOR')

num1=int(input('Enter the 1st number >> '))
oper=str(input('Enter the your opretor >> '))
num2=int(input('Enter the 2nd number >> '))


add='+'
sub='-'
multi='*'
div='/'
if oper==add:
    print('The addition of number is ',num1+num2)
elif oper==sub:
    print('The subtraction of number is ',num1-num2)
elif oper==multi:
    print('The multiplication of number is ',num1*num2)
elif oper==div:
    print('The division of number is ',num1/num2)
else:
    print('invalid opertor')
    print('You will choose this opertors only >>(/,*,-,+)')