import math


def carton():
    cartons = 20
    total = 24 * cartons
    sold = int(input("number of pieces sold:" ))
    if sold < 480 and sold > 0:
        cartons -= 1
        total = 24 * cartons
        left = total - sold
        cartons = left/24
        print("{} cartons and {} pieces left".format(math.ceil(cartons), math.ceil(cartons)%sold))
    # elif sold < 480:
    #     cartons = 20
    #     pieces = 24 * cartons
    #     print("{} cartons and {} pieces left".format(math.ceil(cartons), 480-sold))
    else:
        exit(1)

carton()