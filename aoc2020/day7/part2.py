def create_dictionary(puzzle_input: str) -> dict:
    color_dict = {}
    rules = puzzle_input.splitlines()

    for rule in rules:
        container_rule = rule.split(" bags contain ")
        inside_rules = container_rule[1].split(", ")
        color_dict[container_rule[0]] = {}

        for inside_rule in inside_rules:
            inside_rule = inside_rule.split(" ")
            if inside_rule[0] == "no":
                color_dict[container_rule[0]] = {}
            else:
                color_dict[container_rule[0]][f"{inside_rule[1]} {inside_rule[2]}"] = int(inside_rule[0])

    return color_dict


def count_bags(rules: dict, outer: str) -> int:
    count = 0

    if len(rules[outer]):
        for inner in rules[outer]:
            count += rules[outer][inner]
            count += rules[outer][inner] * count_bags(rules, inner)
        return count
    else:
        return 0


def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    color_dict = create_dictionary(puzzle_input)

    print(f"Shiny gold bag must contain {count_bags(color_dict, 'shiny gold')} other bags.")


if __name__ == "__main__":
    main()
