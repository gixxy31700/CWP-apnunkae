import sys
from checkmate import checkmate


def main():
    if len(sys.argv) < 2:
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, "r") as file:
                board = file.read().rstrip("\n")

            rows = board.splitlines()

            if not rows or any(len(row) != len(rows) for row in rows):
                print("Error")
                continue

            if sum(row.count("K") for row in rows) != 1:
                print("Error")
                continue

            print("Success" if checkmate(board) else "Fail")

        except Exception:
            print("Error")


if __name__ == "__main__":
    main()