print("(1) First Free Service")
print("(2) Second Free Service")

A = int(input("Enter The Free Service Number: "))
K = int(input("Enter Number Of Miles: "))

if A == 1:
    if K > 1500 and K <= 3000:
        print("Vehicle Must Be Service")
    else:
        print("you're vehicle do not need to be serviced")
elif A == 2: 
    if K > 3001 and K <= 4500:
        print("Vehicle Must Be Service")
    else:
        print("you're vehicle do not need to be serviced")

