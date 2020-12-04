with open("input.txt") as f:
    lines = f.readlines()

valid_pass_count = 0

for line in lines:
    splitted = line.split()

    how_much = splitted[0].split("-")
    letter = splitted[1][:1]

    first_letter_check = splitted[2][int(how_much[0]) - 1]
    second_letter_check = splitted[2][int(how_much[1]) - 1]

    if (
        first_letter_check == letter
        and second_letter_check != letter
        or first_letter_check != letter
        and second_letter_check == letter
    ):
        valid_pass_count = valid_pass_count + 1

print(valid_pass_count)
