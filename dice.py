import random
response = input("Do you want to start the dice(Y/y or N/n):")
while(response == 'Y' or response == 'y'):
    no = random.randint(1,6)
    if(no == 1):
        print(["   "])
        print([" 0 "])
        print(["   "])
    elif(no == 2):
        print(["0  "])
        print(["   "])
        print(["  0"])
    elif(no == 3):
        print(["0  "])
        print([" 0 "])
        print(["  0"])
    elif(no == 4):
        print(["0 0"])
        print(["   "])
        print(["0 0"])
    elif(no == 5):
        print(["0 0"])
        print([" 0 "])
        print(["0 0"])
    elif(no == 6):
        print(["0 0"])
        print(["0 0"])
        print(["0 0"])
    response = input("Do you want to continue(Y/y or N/n): ")
print("Thank you")

