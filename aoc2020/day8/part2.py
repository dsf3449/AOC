import copy

def does_loop(puzzle_input):
    acc = 0
    line = 0
    visited_lines = []

    while line in range(0, len(puzzle_input)):
        if line in visited_lines:
            print(f"Repeated command found, acc: {acc}, line: {line}")
            return True
        visited_lines.append(line)

        opcode = puzzle_input[line]
        split = opcode.split(" ")

        if split[0] == "acc":
            acc += int(split[1])
        elif split[0] == "jmp":
            line += int(split[1])
            continue

        line += 1

    return False


def calculate_acc(puzzle_input):
    count = 0
    acc = 0

    while count in range(0, len(puzzle_input)):
        line = puzzle_input[count].split(" ")

        if line[0] == "acc":
            acc += int(line[1])
        elif line[0] == "jmp":
            line += int(line[1])
            continue

    return acc


def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    puzzle_input = puzzle_input.splitlines()
    i = 0

    while i in range(0, len(puzzle_input)):
        line = puzzle_input[i]
        split_line = line.split(" ")
        puzzle_copy = copy.deepcopy(puzzle_input)

        if split_line[0] == "jmp":
            puzzle_copy[i] = f"nop {split_line[1]}"
        elif split_line[0] == "nop":
            puzzle_copy[i] = f"jmp {split_line[1]}"

        if does_loop(puzzle_copy):
            i += 1
            continue
        else:
            print(f"Inverting line {i} fixed it, acc: {calculate_acc(puzzle_copy)}")
            break


if __name__ == "__main__":
    main()
