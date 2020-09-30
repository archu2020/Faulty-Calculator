# This programme is a faulty calculator all clculation will correct except fllowings this ones:
# 4*55=687, 89-123=569,58+90=154,5696/82=954

inp1=int(input("Please Enter your 1st Number\n"))
inp2=input("Please Enter your Operator\n")
inp3=int(input("Please Enter your 2nd Number\n"))

if inp1 == 4 and inp3 == 55 and inp2 == "*":
    print("The ans is 689")
    print("This calculation is wrong please try again")

elif inp1 == 89 and inp3 == 123 and inp2 == "-":
    print("The ans is 569")
    print("This calculation is wrong please try again")

elif inp1 == 58 and inp3 == 90 and inp2 == "+":
    print("The ans is 154")
    print("This calculation is wrong please try again")

elif inp1 == 5696 and inp3 == 82 and inp2 == "/":
    print("The ans is 945")
    print("This calculation is wrong please try again")

elif inp2 == "*":
    print("The Ans is",inp1 * inp3)

elif inp2 == "-":
    print("The Ans is",inp1 - inp3)

elif inp2 == "+":
    print("The Ans is",inp1 + inp3)

elif inp2 == "/":
    print("The Ans is",inp1 / inp3)
else:
    print("Wrong input , Please try again later")
