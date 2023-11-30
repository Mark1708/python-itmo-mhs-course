import sys
from pathlib import Path


def count_stat(content):
    return (len(content.splitlines()),
            len(content.split()),
            len(content.encode('utf-8')))


def print_stat(lines, words, bytes, file_path, is_total):
    if (file_path == ""):
        if is_total:
            print(f" {lines} {words} {bytes} total")
        else:
            print(f" {lines}\t{words}\t{bytes}")
    else:
        print(f" {lines} {words} {bytes} {file_path}")


if __name__ == "__main__":
    files = sys.argv[1:]

    if not files:
        content = sys.stdin.read()
        lines, words, bytes = count_stat(content)
        print_stat(lines, words, bytes, "", False)
    else:
        total_lines, total_words, total_bytes = 0, 0, 0

        for file_path in files:
            lines, words, bytes = count_stat(Path(file_path).read_text())
            total_lines += lines
            total_words += words
            total_bytes += bytes
            print_stat(lines, words, bytes, file_path, False)

        if len(files) > 1:
            print_stat(total_lines, total_words, total_bytes, "", True)
