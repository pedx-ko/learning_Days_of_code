import json


info = {"object1": {'name': 'John Doe', 'age': 20, 'courses': ['Math', 'Science', 'English']},
        "object2": {'name': 'Maria Doe', 'age': 29, 'courses': ['Mathw', 'Sciencea', 'ROM']}
        }

travel_info = {
    'Paris': [{"object1": {'name': 'John Doe', 'age': 20, 'courses': ['Math', 'Science',
                                                                      'English']}},
              {'name': 'Eiffel Tower',
              'description': 'Iconic landmark in Paris, France',
               'address': '5 Avenue Anatole France, 75007 Paris'}],
    'Rome':
        {'name': 'Colosseum',
         'description': 'Ancient amphitheater in Rome, Italy',
         'address': 'Piazza del Colosseo, 00187 Roma'},
    'Tokyo':
        {'name': 'Shibuya Crossing',
         'description': 'Busy intersection in Tokyo, Japan',
         'address': '1-21 Shibuya, 150-0002 Tōkyō'}
}


travel_info.update({'New Paris': travel_info.pop('Paris')})
travel_info = list(travel_info)
# sorted(travel_info.items())

print((travel_info))
