def reverse(sentence, reverse_word):
    #print(reverse_word[::-1])
    if type(reverse_word)!=str:
        return "invalid input"
    if sentence.find(reverse_word) == -1:
        return "The word was not found"
    return(sentence.replace(reverse_word, reverse_word[::-1], 1))


print(reverse("I like apples and I also like bananas", "like"))
print(reverse("I like apples and I also like bananas", "oranges"))
print(reverse("I like apples and I also like bananas", "Bananas"))
print(reverse("I like apples and I also like bananas", 3))

