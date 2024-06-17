import random

min_number = 1
max_number = 45
numbers_per_pick = 6
num_picks = int(input("How many quick picks? "))
for i in range(num_picks):
    quick_pick = []
    while len(quick_pick) < numbers_per_pick:
        number = random.randint(min_number, max_number)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))
