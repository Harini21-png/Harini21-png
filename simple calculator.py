print("simple calculator")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.divide")
choice=input("enter a number:")
num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))
if choice=='1':
    print("The answer is:",num1+num2)
elif choice=='2':
    print("The answer is:",num1-num2)
elif choice=='3':
    print("The answer is:",num1*num2)
elif choice=='4':
    print("The answer is:",num1/num2)
else:
    print("invalid input")