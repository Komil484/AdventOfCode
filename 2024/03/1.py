import re

total = 0
with open("input.txt", "r") as file:
    total = 0
    do = True
    for line_no, line in enumerate(file):
        for rgx_match in re.finditer(
            r"mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)",
            line,
        ):
            a, b = int(rgx_match["num1"]), int(rgx_match["num2"])
            total += a * b
print(total)
