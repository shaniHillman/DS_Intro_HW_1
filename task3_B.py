
def findShortest(lst):
    length = len(lst)
    short = len(lst[0])
    ret = 0
    for x in range(0, length):
        if len(lst[x]) < short:
            short = len(lst[x])
            ret = x
    return ret

def longest_words(file):
    try:
        lst_max = ["", "", "", "", ""]
        fhand = open(file)
        for line in fhand:
            #print(line)
            for word in line.split():
                #print(word)
                index = findShortest(lst_max)
                if len(word) > len(lst_max[index]):
                    lst_max[index]=word
        return(lst_max)
    except:
        print("file not found")

# print(longest_words('ex3_text.txt'))
# longest_words('ex4_text.txt')
