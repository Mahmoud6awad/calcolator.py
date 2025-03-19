import os
os.system('cls'if os.name == 'nt'else 'clear')

print("the operators is  :  (/,*,-,+,^,%)")

num1 =float(input("enter the number1  :  "))

operator =input("enter yor operators  :  ")

num2 =float(input("enter the number2  :  "))

if operator =="+":

    print( "the number1 + number2  =  ",num1+num2)

elif operator =="-":

    print("the number1  + number2  =  ",num1-num2)

elif operator =="*":

    print("the number1  + number2  =  ",num1*num2)

elif operator =="/":

    print("the number1  + number2  =  ",num1/num2)   

elif operator =="^":

    square= num1**num2

    print("the square of number1  =   ",square)

elif operator =="%":

    mod=num1%num2

    print("the number1 % number2  =   ",mod)
    