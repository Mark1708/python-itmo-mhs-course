import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        else:
            lines = sys.stdin.readlines()

        for i, line in enumerate(lines, start=1):
            if line.strip():
                print(f"{i}\t{line.rstrip()}")
    else:
        print("Укажите как аргумент путь до файла")
