import sys
from checkmate import evaluate_board
 
def read_board_file(path):
    """Read a board from a file path.
    Returns the file's content as a string, or None if the file can't
    be read for any reason (missing, is a directory, permission denied,
    not decodable as text, etc.) so the caller never has to deal with
    an exception directly.
    """
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception:
        return None
 
 
def process_file(path):
    """Return "Success", "Fail", or "Error" for one board file."""
    content = read_board_file(path)
    if content is None:
        return "Error"
    return evaluate_board(content)
 
 
def main():
    if len(sys.argv) < 2:
        print("Error")
        return
 
    for path in sys.argv[1:]:
        print(process_file(path))
 
 
if __name__ == "__main__":
    main()
 