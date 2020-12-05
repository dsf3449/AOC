def main():
    invalid_passports = 0
    valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    with open("input.txt") as file:
        puzzle_input = file.read()
        passports = puzzle_input.split("\n\n")

        for passport in passports:
            passport_is_valid = True

            for field in required_fields:
                if field not in passport:
                    passport_is_valid = False
                    invalid_passports += 1
                    break

            if passport_is_valid:
                valid_passports += 1

    print(f"Valid passports: {valid_passports}, invalid passports: {invalid_passports}.")


if __name__ == "__main__":
    main()
