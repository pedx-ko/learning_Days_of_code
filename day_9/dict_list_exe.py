list_of_countrys = [
    {"country": "France", "visits": 5, "cities": [
        "Paris", "Lyon", "Marseille"]},
    {"country": "Germany", "visits": 7, "cities": [
        "Berlin", "Hamburg", "Munich"]},
]


def addin_new_contry(add_new):
    add_new = list(add_new)  # Convert tuple to list for easier manipulation
    x = 0
    disi = {}
    for key in list_of_countrys[0]:
        # Create a new dictionary with the country data
        disi.update({key: add_new[x]})
        x += 1
    list_of_countrys.append(disi)  # Adding dict to the main list of countries
    print(list_of_countrys)


# Adding new country to the list of countries
add_new = ("Italy", 3, ["Rome", "Milan", "Venice"])
addin_new_contry(add_new)
