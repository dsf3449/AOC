def traverse_map(puzzle_input: str, right: int, down: int) -> tuple:
    list_of_nums = puzzle_input.split("\n")

    row = 0
    column = 0
    number_of_trees = 0
    number_of_open = 0

    while row < len(list_of_nums) - 1:
        column += right
        if column > 30:
            column -= 31

        row += down

        if list_of_nums[row][column] == "#":
            number_of_trees += 1
        else:
            number_of_open += 1

    return number_of_trees, number_of_open


def main():
    file = open("input.txt", "r")
    puzzle_input = file.read()
    file.close()

    questions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    solution = 1

    for question in questions:
        number_of_trees, number_of_open = traverse_map(puzzle_input, question[0], question[1])
        print(f"{question[0]}x{question[1]}: number of trees: {number_of_trees}, number of open: {number_of_open}")
        solution *= number_of_trees

    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
