num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
total = num1+num2
answer = input("Do you want to add another number?y/n")
if answer == "y":
    num3 =  int(input("Enter the number:"))
    total+=num3
print(total)