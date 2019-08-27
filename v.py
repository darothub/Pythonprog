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
    spchr =[]

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
            
            spchr.append(x)
    print(index_keys)
    for h in keys:
        
        keydup.append(alpha.index(h))
        keydup2 = keydup
    print(keydup)
 
    for j in range(length):
        index_keys.insert(j, keydup[j])
        # print (index_keys)
        word = (index_keys[j]+index_keys[j+1])
        print(word, end = ' ')
        index_text.append(word)
        index_keys = index_keys[1:]
        keydup.append(keydup[j])
    print(index_text)
    for k in index_text:
        print(alpha[k], end= ' ')





vigenere()