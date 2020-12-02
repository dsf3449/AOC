def find_summation(list_of_nums):
    for number1 in list_of_nums:
        for number2 in list_of_nums:
            for number3 in list_of_nums:
                if int(number1) + int(number2) + int(number3) == 2020:
                    return [int(number1), int(number2), int(number3)]


def main():
    file = open("day1_input.txt", "r")
    puzzle_input = file.read()
    file.close()
    list_of_nums = puzzle_input.split("\n")
    two_nums = find_summation(list_of_nums)
    print(f"Answer: {two_nums[0] * two_nums[1] * two_nums[2]}")


if __name__ == "__main__":
    main()
