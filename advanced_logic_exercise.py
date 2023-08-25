# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_ints = []
for number in numbers:
    if number % 2 == 0:
        even_ints.append(number)
print(even_ints)

# 2. Print the difference between the largest and smallest value:

sorted_list = sorted(numbers)
print(sorted_list[-1] - sorted_list[0])

# 3. Print True if the list contains a 2 next to a 2 somewhere.

previous_num = None
for number in numbers:
    if number == 2 and previous_num == 2:
        print(True)
    previous_num = number


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

between_6_and_7 = False
print(numbers)
total = 0
for number in numbers:
    if number == 6:
        between_6_and_7 = True
    if between_6_and_7 == False:
        total += number
    if number == 7:
        between_6_and_7 = False
print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

previous_num = None
total = 0
for number in numbers:
    if number != 13 and previous_num != 13:
        total += number
    previous_num = number
print(total)
# i feel a little uneasy about this because it felt easier than 
# the last question and also i don't think i've tracked the index at all,
# but i'm pretty sure it works anyway?