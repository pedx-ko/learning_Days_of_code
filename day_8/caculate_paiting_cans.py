'numebers of cans = (wall height x wall widtth) / converrage per can'

import math


def num_cans(W_heigth=2, W_width=2, W_cove=5):
    # W_area =
    result = math.ceil((W_heigth * W_width)/W_cove)
    print(f" Your Area is {result}")


num_cans(5, 5.4, 5)
