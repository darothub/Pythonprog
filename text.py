# import re
# xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
# print(sorted(xs.items(), key=lambda x: x[1]))

# print(re.escape("python.exe"))


# def reader():
#     setter1 = set()
#     setter2 = set()

#     file1 = open('read.txt', 'r').readlines()
#     file2 = open('read2.txt', 'r').readlines()
#     for i in file2:
#         if(file1.index(i)):
#             setter1.add(i.strip('\n'))
#     return setter1

# print(reader())
# from nltk.tokenize import sent_tokenize

# a = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy. only gonna play the fool one time"
# b = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
# c = set(sent_tokenize(a))
# d = set(sent_tokenize(b))
# similar = c | d
# print(list(similar))



# def sub(a, n):
#     m = n
#     string = []
#     final = []
#     for i in range(len(a)):
#         string.append(a[i:n])
#         n +=1
#     final = [x for x in string if len(x)== m]
#     # for i in string:
#     #     if len(i) == m:
#     #         final.append(i)
    
#     return final
    

# print(sub("hello", 2))


def sub():
    tup = ( 0, 2, 3, 4, 5, None)
    for i in tup:
        if i == None:
            return i
    
    print('end')

sub()