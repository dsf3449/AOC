def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    puzzle_input = puzzle_input.splitlines()
    starting = 0

    while starting in range(0, len(puzzle_input)):
        range_to_look = puzzle_input[starting:starting + 25]
        did_find_pair = False

        for outer in range_to_look:
            for inner in range_to_look:
                if int(outer) + int(inner) == int(puzzle_input[starting + 26]):
                    did_find_pair = True

        if not did_find_pair:
            print(puzzle_input[starting + 26])
            return

        starting += 26


if __name__ == "__main__":
    main()
