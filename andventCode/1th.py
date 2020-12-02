with open("input.txt") as f:
    lines = f.readlines()

numbers = []

for line in lines:
    numbers.append(line.rstrip())


firstVal = 0

for i in range(0, len(numbers)):
    firstVal = numbers[i]
    for j in range(0, len(numbers)):
        sum = int(firstVal) + int(numbers[j])
        if sum == 2020:
            result = int(firstVal) * int(numbers[j])

print("Done! You number is ", result)
