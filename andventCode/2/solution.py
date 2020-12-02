with open("input.txt") as f:
    lines = f.readlines()

valid_pass_count = 0
for line in lines:
    splitted = line.split()

    how_much = splitted[0].split("-")
    letter = splitted[1][:1]
    count_letter = splitted[2].count(letter)

    if count_letter >= int(how_much[0]) and count_letter <= int(how_much[1]):
        valid_pass_count = valid_pass_count + 1

print(valid_pass_count)
