our_string = input("enter your string: ")

#A
sentences = our_string.split(".")
words = our_string.split(" ")

print(f"number of sentences is {len(sentences)}")
print(f"number of words is {len(words)}")

#B
for vowel in ["a","o","i","e","u"]:
    print(f"number of {vowel} is {our_string.count(vowel)}")

#C
search_word = input("enter a word to check if it exist's in the string: ")

if search_word in our_string:
    print(f"yes it is on index {our_string.index(search_word)}")
else:
    print("this word doesn't exist!!")

# I'll also push these exercises into my github on "https://github.com/HoutanTV/guilan-boron-exerxises"