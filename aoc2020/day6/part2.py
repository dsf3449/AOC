def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    groups = puzzle_input.split("\n\n")
    sum_of_answers = 0

    for group in groups:
        size_of_group = group.count("\n") + 1
        group = "".join(group.splitlines())
        answer_list = []

        for answer in group:
            if group.count(answer) != size_of_group or answer in answer_list:
                continue
            else:
                answer_list.append(answer)

        sum_of_answers += len(answer_list)

    print(f"Sum of answers: {sum_of_answers}")


if __name__ == "__main__":
    main()
