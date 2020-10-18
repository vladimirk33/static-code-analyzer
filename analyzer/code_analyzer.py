def line_length_check(file):
    for line_num, line in enumerate(file):
        if len(line) > 79:
            print(f"Line {line_num + 1}: S001 Too long")


def main():
    with open(input(), "r") as file:
        line_length_check(file)


if __name__ == "__main__":
    main()
