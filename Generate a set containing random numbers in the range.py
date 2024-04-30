import random
# Generate a set containing 10 random numbers in the range of 15 to 45
random_numbers_set = set()
while len(random_numbers_set) < 10:
    random_number = random.randint(15, 45)
    random_numbers_set.add(random_number)

print("Original set of random numbers:", random_numbers_set)

# Count how many numbers are less than 30
count_less_than_30 = sum(1 for num in random_numbers_set if num < 30)
print("Count of numbers less than 30:", count_less_than_30)



# Delete all the numbers less than 30 from the set
random_numbers_set = {num for num in random_numbers_set if num >= 30}

print("Set after deleting numbers less than 30:", random_numbers_set)
