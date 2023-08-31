while True:
    num1=float(input("enter the value for 1:"))
    num2=float(input("enter the value for 2:"))
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    
    print('1)Addition \n2)substraction \n3)multiplication \n4)division')
    choice=int(input('Enter your choice: '))
    if (choice==1):
        print(add)
    
    elif(choice==2):
        print(sub)
    elif(choice==3):
        print(mul)
    elif(choice==4):
        print(div)
    else:
        print("invaild value")
