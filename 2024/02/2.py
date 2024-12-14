total = 0
with open("input.txt", "r") as file:
    for line_no, line in enumerate(file):
        prev_total = total
        nums = [int(num) for num in line.split()]

        for i in range(len(nums)):
            nums_temp = nums.copy()
            nums_temp.pop(i)

            if len(nums_temp) == 1:
                total += 1
                break

            diff = nums_temp[0] - nums_temp[1]
            if diff == 0 or not (1 <= abs(diff) <= 3):
                continue

            direction = 1 if diff > 0 else -1

            for i in range(1, len(nums_temp) - 1):
                diff = nums_temp[i] - nums_temp[i + 1]
                if not (1 <= diff * direction <= 3):
                    break
            else:
                total += 1
                break

print(total)
