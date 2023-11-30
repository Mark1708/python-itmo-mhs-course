import sys


def print_lines(lines, size):
    start_index = max(0, len(lines) - size)
    for line in lines[start_index:]:
        print(line, end='')
    print()


def print_file(file_path):
    with open(file_path, 'r') as file:
        print_lines(
            file.readlines(),
            10
        )


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        lines = []
        size = 17
        for _ in range(size):
            lines.append(sys.stdin.readline())
        print("==> stdin <==")
        print_lines(lines, size)
    else:
        if len(files) == 1:
            print_file(files[0])
        else:
            for file_path in files:
                print(f"==> {file_path} <==")
                print_file(file_path)
