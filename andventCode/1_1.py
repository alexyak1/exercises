numbers = []

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    numbers.append(line.rstrip())


for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        for k in range(0, len(numbers)):
            sum = int(numbers[i]) + int(numbers[j]) + int(numbers[k])
            if sum == 2020:
                print(numbers[i])
                print(numbers[j])
                print(numbers[k])
                print("--------")
                result = int(numbers[i]) * int(numbers[j]) * int(numbers[k])

print("Done! You number is ", result)
