numbers_count = int(input("how many numbers do you want to add?: "))
our_list = []

for i in range(numbers_count):
    new_number = int(input(f"enter the #{i+1} number: "))
    our_list.append(new_number)

even_list = []
for num in our_list:
    if num % 2 ==0:
        even_list.append(num)

print("even numbers are",*even_list)

# I'll also push these exercises into my github on "https://github.com/HoutanTV/guilan-boron-exerxises"