numbers_count = int(input("how many sentences do you want to add?: "))
our_list = []

for i in range(numbers_count):
    new_sentence = input(f"enter the #{i+1} sentence: ")
    our_list.append(new_sentence)

output_list = []
for i in our_list:
    if len(i) > 5:
        output_list.append(i)

print("resault is",output_list)

# I'll also push these exercises into my github on "https://github.com/HoutanTV/guilan-boron-exerxises"