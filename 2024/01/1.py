l1 = []
l2 = []
with open("input.txt", "r") as file:
    for line in file:
        num1, *_, num2 = line.strip().split(" ")
        num1, num2 = int(num1), int(num2)
        l1.append(num1)
        l2.append(num2)

l1.sort()
l2.sort()

total_diff = 0
for num1, num2 in zip(l1, l2):
    total_diff += abs(num1 - num2)
print(total_diff)
