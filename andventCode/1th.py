numbers = []

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    numbers.append(line.rstrip())


for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        sum = int(numbers[i]) + int(numbers[j])
        if sum == 2020:
            result = int(numbers[i]) * int(numbers[j])

print("Done! You number is ", result)
