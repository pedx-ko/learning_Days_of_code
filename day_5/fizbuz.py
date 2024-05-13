import imaplib


target = 100

for nimber in range(1,(target+1)):
    if nimber % 3 == 0 and nimber % 5 == 0:
        # print(nimber)
        print("Fizz Buss")
    elif nimber % 3 == 0 and nimber % 5 !=0:
        # print(nimber)
        print("Fizz")
    elif nimber % 5 == 0 and nimber % 3 !=0:
        # print(nimber)
        print("Buzz")
    else:
        print(nimber)