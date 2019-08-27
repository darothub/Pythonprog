from sys import argv

def caesar():
    key = argv[1]
    plaintext = input("plaintext: ")
    length = len(plaintext)
    for x in range(length):
        letter = plaintext[x]
        convert = ord(letter)
        word = ''
        if (convert >= 65 and convert < 90):
            convert = convert + int(key)

            if(convert > 90):
                convert = convert - 90
                convert = convert + 64
                word += chr(convert)
            else:
                word +=chr(convert)
                
        elif (convert >= 97 and convert < 122):
                convert = convert + int(key)
    
                if(convert > 122):
                    convert = convert - 122
                    convert = convert + 96
                    word += chr(convert)
                else:
                    word +=chr(convert)
                   
        else:
            word += chr(convert)
            
        print(word, end='')

    


caesar()