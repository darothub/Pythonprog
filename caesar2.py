from sys import argv

def caesar():
    if len(argv) <= 1:
        exit(1)
    key = int(argv[1])
    plaintext = input("plaintext: ")
    length = len(plaintext)
    char =''
    word =''
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in plaintext:
        if x in lower:
            index = lower.index(x) + key
            while index >= 25:
                index -= 26
                # word +=lower[index]
                # print(word, end='')
            word +=lower[index]
        elif x in upper:
            index = upper.index(x) + key
            if index > 25:
                index -= 26
                # word +=upper[index]
                # print(word, end='')
            word +=upper[index]
        else:
            word += x
    print("ciphertext: {}".format(word), end ='\n')
caesar()