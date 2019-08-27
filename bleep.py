# from cs50 import get_string
from sys import argv


def main():

    # TODO

    while len(argv)<=1 or len(argv)> 2:
        print('Usage: python bleep.py dictionary')
        exit(1)

    dictionary = argv[1]
    message = input("What message would you like to censor?")
    message_split = message.split(' ')
    file = open(dictionary, 'r')
    wordlist = set()
    banned = ()
    bannedlist = []
    for x in file:
        wordlist.add(x.strip('\n'))

    for y in message_split:
        if y in wordlist:
            banned = (y, '*'*len(y))
            bannedlist.append(banned)
            continue
        else:
            continue
    for z in bannedlist:
        message = message.replace(*z)
    print(message)


if __name__ == "__main__":
    main()
