def main():
    file = open("input.txt", "r")
    puzzle_input = file.read()
    file.close()

    list_of_nums = puzzle_input.split("\n")
    row = 0
    column = 0
    number_of_trees = 0
    number_of_open = 0

    while row < len(list_of_nums) - 1:
        column += 3
        if column > 30:
            column -= 31

        row += 1

        if list_of_nums[row][column] == "#":
            number_of_trees += 1
        else:
            number_of_open += 1

    print(f"Number of trees: {number_of_trees}, number of open: {number_of_open}")


if __name__ == "__main__":
    main()
