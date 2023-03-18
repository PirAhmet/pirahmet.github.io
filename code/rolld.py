def roll_dice(num_dice):
    import random
    return [random.randint(1, 6) for _ in range(num_dice)]

rolls = []
for i in range(6):
    num_dice = int(input(f"How many dice for roll {i+1}? (3-9): "))
    while num_dice < 3 or num_dice > 9:
        num_dice = int(input(f"Invalid input. How many dice for roll {i+1}? (3-9): "))
    rolls.append(roll_dice(num_dice))

for roll in sorted(rolls, key=lambda x: sum(x), reverse=True):
    print(f"{roll}: {sum(sorted(roll, reverse=True)[:3])}")

