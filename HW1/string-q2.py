first_word = input("please enter the first word: ")
second_word = input("please enter the second word: ")
third_word = input("please enter the third word: ")

output_str = ""

for word in [first_word,second_word,third_word]:
    if len(word) % 2 == 1:
        wanted_index = len(word) // 2
        output_str += word[wanted_index]
    else:
        output_str += word[1]

print(output_str)

# I'll also push these exercises into my github on "https://github.com/HoutanTV/guilan-boron-exerxises"