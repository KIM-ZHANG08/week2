total=0
for i in range(5):
    number=int(input("Enter a number:"))
    answer=input("if you want the number to be included?")
    if answer=="yes":
        total+=number
print("The total number is:",total)

