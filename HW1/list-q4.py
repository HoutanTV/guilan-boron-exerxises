numbers_count = int(input("how many numbers do you want to add?: "))
our_list = []

for i in range(numbers_count):
    new_number = int(input(f"enter the #{i+1} number: "))
    our_list.append(new_number)

resault = 1

for i in range(3):
    max_num = max(our_list)
    resault *= max_num
    our_list.pop(our_list.index(max_num))

print("the resault is:",resault)

# I'll also push these exercises into my github on "https://github.com/HoutanTV/guilan-boron-exerxises"