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


def recursive_search(rules: dict, outer: str, track: list) -> bool:
    if "shiny gold" in rules[outer]:
        return True
    else:
        for inner in rules[outer]:
            if inner not in track:
                track.append(inner)
                if recursive_search(rules, inner, track):
                    return True
        return False


def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    color_dict = create_dictionary(puzzle_input)
    total = 0

    for color in color_dict:
        track = []
        if recursive_search(color_dict, color, track):
            total += 1

    print(f"Total number of bags that can contain a shiny gold bag: {total}")


if __name__ == "__main__":
    main()
