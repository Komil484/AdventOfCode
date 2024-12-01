d1 = dict()
d2 = dict()
with open("input.txt", "r") as file:
    for line in file:
        num1, *_, num2 = line.strip().split(" ")
        num1, num2 = int(num1), int(num2)
        d1[num1] = d1.get(num1, 0) + 1
        d2[num2] = d2.get(num2, 0) + 1

total_similarity = 0

for num, count in d1.items():
    total_similarity += num * d2.get(num, 0) * count

print(total_similarity)
