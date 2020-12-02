def main():
    invalid_passwords = 0
    valid_passwords = 0

    with open("input.txt") as file:
        for line in file:
            split_line = line.split(" ")
            range_of_occurrences = split_line[0].split("-")
            char_to_look_for = split_line[1][:-1]
            password = split_line[2].rstrip()
            occurrences_of_char = password.count(char_to_look_for)

            if occurrences_of_char not in range(int(range_of_occurrences[0]), int(range_of_occurrences[1]) + 1):
                invalid_passwords += 1
            else:
                valid_passwords += 1

    print(f"Valid passwords: {valid_passwords}, invalid passwords: {invalid_passwords}")


if __name__ == "__main__":
    main()
