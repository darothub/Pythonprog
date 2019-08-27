import math
def luhn():
    adder = 0
    multlist =[]
    card = int(input("card number: "))
    strcard = str(card)
    strlen = len(strcard)
    
    if(strlen < 13 or strlen == 14 or strlen > 16):
        print("INVALID", end='\n')
        return False
    counter = math.ceil(strlen/2)
    # print(counter)
    count = strlen-2
    while count >= 0:
        multlist.append(int(strcard[count])*2)
        count = count - 2
    print(multlist)
    for y in range(len(multlist)):
        if multlist[y] > 9:
           print(multlist[y])
           adder+=multlist[y] - 9
        else:
            adder += multlist[y]
    print(adder)
    for z in range(strlen-1, -1, -2):
        adder+=int(strcard[z])
    print(adder)
    if adder % 10 == 0:
        if int(strcard[0]) == 4:
            print("VISA")
            
        elif int(strcard[0]) == 3 and (int(strcard[1]) == 4 or int(strcard[1]) == 7):
            print("AMEX")
            
        elif int(strcard[0]) == 5 and (int(strcard[1]) in range(1, 6)):
            print("MASTERCARD") 
        else:
            print("INVALID")

    else:
        print("INVALID")



luhn()