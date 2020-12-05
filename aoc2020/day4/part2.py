import re


def main():
    invalid_passports = 0
    valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    with open("input.txt") as file:
        puzzle_input = file.read()
        passports = puzzle_input.split("\n\n")

        for passport in passports:
            passport_is_valid = True
            passport = " ".join(passport.splitlines())
            passport_raw_attributes = passport.split(" ")
            passport_attributes = {}

            for attribute in passport_raw_attributes:
                holder = attribute.split(":")
                passport_attributes[holder[0]] = holder[1]

            for field in required_fields:
                if field not in passport:
                    passport_is_valid = False
                    print(f"Passport not valid, reason: missing required field {field}")

            for attribute in passport_attributes:
                if attribute == "byr":
                    if int(passport_attributes[attribute]) not in range(1920, 2003):
                        passport_is_valid = False
                        print(f"Passport not valid, reason: birth year {passport_attributes[attribute]} not between 1920 and 2002")
                elif attribute == "iyr":
                    if int(passport_attributes[attribute]) not in range(2010, 2021):
                        passport_is_valid = False
                        print(f"Passport not valid, reason: issue year {passport_attributes[attribute]} not between 2010 and 2020")
                elif attribute == "eyr":
                    if int(passport_attributes[attribute]) not in range(2020, 2031):
                        passport_is_valid = False
                        print(f"Passport not valid, reason: expiration year {passport_attributes[attribute]} not between 2020 and 2030")
                elif attribute == "hgt":
                    if "cm" in passport_attributes[attribute]:
                        height = int(passport_attributes[attribute][:-2])
                        if height not in range(150, 194):
                            passport_is_valid = False
                            print(f"Passport not valid, reason: CM height {passport_attributes[attribute]} not between 150 and 193")
                    elif "in" in passport_attributes[attribute]:
                        height = int(passport_attributes[attribute][:-2])
                        if height not in range(59, 77):
                            passport_is_valid = False
                            print(f"Passport not valid, reason: IN height {passport_attributes[attribute]} not between 59 and 76")
                    else:
                        passport_is_valid = False
                        print(f"Passport not valid, reason: height {passport_attributes[attribute]} is missing measurement style")
                elif attribute == "hcl":
                    if not re.match(r"^#([0-9]|[a-f]){6}$", passport_attributes[attribute]):
                        passport_is_valid = False
                        print(f"Passport not valid, reason: hair color {passport_attributes[attribute]} does not match regex pattern")
                elif attribute == "ecl":
                    if passport_attributes[attribute] not in valid_eye_colors:
                        passport_is_valid = False
                        print(f"Passport not valid, reason: eye color {passport_attributes[attribute]} not valid")
                elif attribute == "pid":
                    if not re.match(r"^\d{9}$", passport_attributes[attribute]):
                        passport_is_valid = False
                        print(f"Passport not valid, reason: passport ID {passport_attributes[attribute]} not 9 digits, is {len(passport_attributes[attribute])}")

            if passport_is_valid:
                valid_passports += 1
            else:
                invalid_passports += 1

    print(f"Valid passports: {valid_passports}, invalid passports: {invalid_passports}.")


if __name__ == "__main__":
    main()
