while True:
        print('''\n Simple Calculator
0 Exit
1 Addition
2 Substration
3 Multiplication
4 Division
5 Percentage''')

        choice=input("enter your choice (1-5)")
        if choice=="0":
                print("Thankyou For Visiting The Calculator, bye-bye")
                break
        if choice in ('1','2','3','4','5'):
                num1=float(input("enter 1st number"))
                num2=float(input("enter 2nd number"))

                if choice=="1":
                        print("result:",num1+num2)
                elif choice=="2":
                        print("result:",num1-num2)
                elif choice=="3":
                        print("result:",num1*num2)
                elif choice=="4":
                        if num2!=0:
                                print("Result:",num1/num2)
                        else:
                                print("Error! Division by zero is not allowed.")
                elif choice=="5":
                        if num2==0:
                                print("not defined")
                        else:
                                percentage=(num1/num2)*100
                                print(f"{num1} is {percentage:.2f}% of {num2}")
                else:
                        print("invalid choice! please select from 1 to 5.")
                        
