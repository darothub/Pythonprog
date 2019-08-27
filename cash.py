def balance():
    balance = round(float(input("balance is:")) * 100)
    while balance <=0:
        print("{} please.".format("balance"))
        balance = round(float(input("balance is:")) * 100)
    counter = 0;
    while balance >= 25:
        # print(balance)
        balance-=25
        counter+=1
    while balance < 25 and balance > 10:
        # print(balance)
        balance -=10
        counter+=1
    while balance <10 and balance > 5:
        # print(balance)
        balance -=5
        counter+=1
    while balance <5 and balance >= 1:
        # print(balance)
        balance -=1
        counter+=1
    print("{}".format(counter))




balance()