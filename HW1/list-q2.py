numbers_count_first = int(input("how many numbers do you want to add for first list?: "))
first_list = []

for i in range(numbers_count_first):
    new_number = int(input(f"enter the #{i+1} number: "))
    first_list.append(new_number)


numbers_count_second = int(input("how many numbers do you want to add for second list?: "))
second_list = []
for i in range(numbers_count_second):
    new_number = int(input(f"enter the #{i+1} number: "))
    second_list.append(new_number)

output_list = []
for i in first_list:
    if i in second_list:
        output_list.append(i)

final_resault = set(output_list) # I did this to prevent duplication in numbers

print("common numbers are",*final_resault)

# I'll also push these exercises into my github on "https://github.com/HoutanTV/guilan-boron-exerxises"