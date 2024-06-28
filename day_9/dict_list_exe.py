'adding a new dict'

list_of_countrys = [
    {"country": "France", "visits": 5, "cities": [
        "Paris", "Lyon", "Marseille"]},
    {"country": "Germany", "visits": 7, "cities": [
        "Berlin", "Hamburg", "Munich"]},
]

# Adding new country to the list of countries
add_new = ("Italy", 3, ["Rome", "Milan", "Venice"])

add_new = list(add_new)  # Convert tuple to list for easier manipulation
x = 0
disi = {}

for key in list_of_countrys[0]:
    x += 1
    # Create a new dictionary with the country data
    disi.update({key: add_new[x]})

list_of_countrys.append(disi)  # Adding dict to the main list of countries
