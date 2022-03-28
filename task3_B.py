def findShortest(lst):
    length = len(lst)
    short = len(lst[0])
    ret = 0
    for x in range(1, length):
        if len(lst[x]) < short:
            short = lst[x]
            ret = x
    return x

print(findShortest(["g","df","hfd"]))

def longest_words(file):
    try:
        lst_max = [None, None, None, None, None]
        fhand=open(file)
        for line in fhand:
            for word in line:
                for word_lst in lst_max:

        if len(word) > len(min):
            word_lst = word



    except:
        return



longest_words("ex3_text.txt")
longest_words("ex4_text.txt")