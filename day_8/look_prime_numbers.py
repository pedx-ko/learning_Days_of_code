'prime numbers can by broken by 1 and it self but nothing else'


# def cheking_Prime(number):

#     # for number in range(1, numbers + 1):
#     look_1 = True
#     look_2 = True
#     for n in range(1, number + 1):
#         if number % 1 == 0 and number % number == 0:
#             look_1 = True
#         if n != number and n != 1:
#             if number % n == 0:
#                 look_2 = False
#             pass

#     if look_1 and look_2:
#         print(f" {number} is a Prime \n")
#     else:
#         print(f" {number} is not a Prime")


# cheking_Prime(75)


# print(9 % 2)


'''testing code profe'''
for number in range(1, 8):
    print(number)
    for i in range(2, number):
        x = True
        if i % i == 0:
            x = False
            # print("no")
        if x:
            print(f"{i} PRime\n")
        else:
            print(f"{i} no prime\n")
