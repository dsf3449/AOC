def find_invalid_number(puzzle_input: list) -> int:
    starting = 0

    while starting in range(0, len(puzzle_input)):
        range_to_look = puzzle_input[starting:starting + 25]
        did_find_pair = False

        for outer in range_to_look:
            for inner in range_to_look:
                if int(outer) + int(inner) == int(puzzle_input[starting + 26]):
                    did_find_pair = True

        if not did_find_pair:
            return int(puzzle_input[starting + 26])

        starting += 26


def find_encryption_weakness(puzzle_input: list, invalid_number: int):
    summed_numbers = []
    total = 0

    for position in range(0, len(puzzle_input)):
        for number in puzzle_input:
            if int(number) == invalid_number:
                continue
            total += int(number)
            summed_numbers.append(int(number))

            if total == invalid_number:
                print(summed_numbers)
                print(sum(summed_numbers))
                print(min(summed_numbers) + max(summed_numbers))
                print(position)
                return

            if total > invalid_number:
                total = 0
                summed_numbers = []

        position += 1
        del puzzle_input[0]


def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    puzzle_input = puzzle_input.splitlines()
    invalid_number = find_invalid_number(puzzle_input)
    find_encryption_weakness(puzzle_input, invalid_number)


if __name__ == "__main__":
    main()
