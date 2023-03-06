our_number = int(input("please enter your number: "))
print(type(our_number))
print(type(str(our_number)))
## or our_number = int(our_number) and for

reversed_number = 0
digit_counts = 0

#counting the digits of number
temp_number = our_number
while True:
    if temp_number == 0:
        break
    digit_counts += 1
    temp_number = temp_number // 10

#generating the reversed number
while True:
    if our_number == 0:
        break
    reversed_number += (our_number % 10) * (10 ** digit_counts)
    digit_counts -= 1
    our_number = our_number // 10

reversed_number /= 10

print(f"reversed number is {int(reversed_number)}")  #adding int is to show it as an integer, bevausse of division it converted into float

# I'll also push these exercises into my github on "https://github.com/HoutanTV/guilan-boron-exerxises"