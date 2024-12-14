total = 0
with open("input.txt", "r") as file:
    for line_no, line in enumerate(file):
        prev_total = total
        nums = [int(num) for num in line.split()]

        if len(nums) < 2:
            if len(nums) > 0:
                total += 1
            continue

        diff = nums[0] - nums[1]
        if diff == 0 or not (1 <= abs(diff) <= 3):
            continue

        direction = 1 if diff > 0 else -1

        for i in range(1, len(nums) - 1):
            diff = nums[i] - nums[i + 1]
            if not (1 <= diff * direction <= 3):
                break
        else:
            total += 1

print(total)
