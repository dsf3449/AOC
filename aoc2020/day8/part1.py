def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    puzzle_input = puzzle_input.splitlines()
    acc = 0
    line = 0
    visited_lines = []

    while line in range(0, len(puzzle_input)):
        if line in visited_lines:
            print(f"Repeated command found, acc: {acc}, line: {line}")
            break
        visited_lines.append(line)

        opcode = puzzle_input[line]
        split = opcode.split(" ")

        if split[0] == "acc":
            acc += int(split[1])
        elif split[0] == "jmp":
            line += int(split[1])
            continue

        line += 1


if __name__ == "__main__":
    main()
