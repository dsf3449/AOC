import math


def value_of_change(iteration: int, which: str) -> int:
    if which == "row":
        return int(64 / math.pow(2, iteration))
    else:
        iteration -= 6
        test = int(8 / math.pow(2, iteration))
        return test


def determine_row(seat: str) -> int:
    row_range = {
        "lower": 0,
        "upper": 127
    }

    for i in range(0, 7):
        if seat[i] == "F":
            row_range["upper"] -= value_of_change(i, "row")
        else:
            row_range["lower"] += value_of_change(i, "row")

    if row_range["lower"] != row_range["upper"]:
        print(f"Unable to determine row for pattern {seat}.")
    else:
        return row_range["lower"]


def determine_column(seat: str) -> int:
    row_range = {
        "lower": 0,
        "upper": 7
    }

    for i in range(7, 10):
        if seat[i] == "L":
            row_range["upper"] -= value_of_change(i, "column")
        else:
            row_range["lower"] += value_of_change(i, "column")

    if row_range["lower"] != row_range["upper"]:
        print(f"Unable to determine column for pattern {seat}.")
    else:
        return row_range["lower"]


def determine_seat(seat: str) -> dict:
    row = determine_row(seat)
    column = determine_column(seat)
    return {
        "row": row,
        "column": column,
        "id": (row * 8) + column
    }


def main():
    with open("input.txt") as file:
        puzzle_input = file.read()

    puzzle_input = puzzle_input.split("\n")
    seat_ids = []

    for seat in puzzle_input:
        seat_position = determine_seat(seat)
        seat_ids.append(seat_position["id"])

    seat_ids.sort()

    for i in range(0, len(seat_ids)):
        if (seat_ids[i - 1] != seat_ids[i] - 1) and (i != 0):
            print(f"Your seat: {seat_ids[i] - 1}")


if __name__ == "__main__":
    main()
