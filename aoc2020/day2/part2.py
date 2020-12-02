def main():
    invalid_passwords = 0
    valid_passwords = 0

    with open("input.txt") as file:
        for line in file:
            split_line = line.split(" ")
            position_of_occurrences = split_line[0].split("-")
            char_to_look_for = split_line[1][:-1]
            password = split_line[2].rstrip()

            first_char = password[int(position_of_occurrences[0]) - 1]
            second_char = password[int(position_of_occurrences[1]) - 1]

            if first_char != char_to_look_for:
                validate_first = False
            else:
                validate_first = True

            if second_char != char_to_look_for:
                validate_second = False
            else:
                validate_second = True

            if (validate_first and validate_second) or (not validate_first and not validate_second):
                invalid_passwords += 1
            else:
                valid_passwords += 1

    print(f"Valid passwords: {valid_passwords}, invalid passwords: {invalid_passwords}")


if __name__ == "__main__":
    main()
