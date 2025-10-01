answer = input("Which direction do you wants to count?up or down:")
if answer == "up":
    topnum = int(input("Enter the top number:"))
    for i in range(1,topnum+1):
        print(i)
elif answer == "down" :
    downnum = int(input("Enter a number below 20:"))
    for i in range(20,downnum-1,-1):
        print(i)
else:
    print("I don't understand")