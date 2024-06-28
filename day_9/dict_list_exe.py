list_of_countrys = [
    {"country": "France", "visits": 5, "cities": [
        "Paris", "Lyon", "Marseille"]},
    {"country": "Germany", "visits": 7, "cities": [
        "Berlin", "Hamburg", "Munich"]},
]


add_new = ("Italy", 3, ["Rome", "Milan", "Venice"])

# add_new = list(add_new)
# print(add_new)

# for i in add_new:
#     list_of_countrys.append(add_new)
# #     # print(i)
# print(list_of_countrys)
# print(add_new[0])


# -----------------try with for loop
add_new = list(add_new)
x = 0
disi = {}
for i in list_of_countrys[0]:  # range(len(add_new)):
    key = i
    elem = add_new[x]
    # print(f"info : {i}  {add_new[x]}")
    x += 1
    disi.update({key: elem})
# -----------------------

# # -----------------try with for loop 2
# disi_list = {}
# add_new = list(add_new)
# x = 0
# disi = {}
# for i in list_of_countrys[0]:  # range(len(add_new)):
#     key = i
#     elem = add_new[x]
#     # print(f"info : {i}  {add_new[x]}")
#     loca = f"{i}: {add_new[x]}"
#     disi_list[]
#     print(loca)
#     x += 1
# # -----------------------

    # list_of_countrys[0][i] = "laca"

    # country = list_of_countrys[i]=

# # try with manual --------------------

# disi = {
#     "country": add_new[0],
#     "visits": add_new[1],
#     "cities": add_new[2],

# }

# #---------
list_of_countrys.append(disi)

print(list_of_countrys)
