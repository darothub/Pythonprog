from sys import argv

def vigenere():
    if len(argv) <= 1:
        exit(1)
    keys = list(argv[1])
    plaintext = input("plaintext: ")
    length = len(plaintext)
    convert = 0
    index_keys = []
    index_text = []
    keydup = []

    word = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    print(keys)

    for x in  plaintext:
        if x.isalpha() and x.isupper():
            # print(upper.index(x))
            index_keys.append(upper.index(x))
        elif x.isalpha():
            # print(alpha.index(x))
            index_keys.append(alpha.index(x))
        else:
            # print(x)
            index_keys.append(upper.index(x))
    print(index_keys)
    for h in keys:
        
        keydup.append(alpha.index(h))
        keydup2 = keydup
    print(keydup)
    for x in keydup:
        index_text = index_keys
        convert =index_text[0] + x
        index_text = index_text[1:]
        print(convert)






vigenere()