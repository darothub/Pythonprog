def marioblock2():
    number = int(input("Number of blocks:"))
    while number <=0 or number > 8:
        number = int(input("Number of blocks:"))
        break
    for x in range(number):
        print(' '*((number-1)-x) + '#'* (x+1) + ' ' + '#'* (x+1))
       
    


marioblock2()