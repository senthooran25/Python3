# def fibbino(num):
#     a = 0
#     b = a+1
#     print(a)
#     print(b)
#     for i in range(num-2):
#         c = a+b
#         print(c)
#         a = b
#         b = c
#
#
# fibbino(8)

# def reverse(name):
#     rev_name =''
#     for a in name:
#         rev_name = a + rev_name
#     print(rev_name)
#
# reverse('hello')

def rev_words(line):
    words = line.split(" ")
    rev_name = []
    rev_list = []
    print(words)
    for w in range(len(words)):
        rev_list = rev_list[w] + words[w]
    rev_name = ' '.join(rev_list)
    print(rev_name)



rev_words("My name is billa")