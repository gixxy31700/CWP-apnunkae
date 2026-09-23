PIECES = "KPBRQ"
 
 
def parse_board(board):
    """Turn the raw board argument into a list of row-strings.
    Returns None if the board is not usable (not a string, empty,
    or not square) so the caller can fail safely instead of crashing.
    """
    if not isinstance(board, str):
        return None
    rows = board.splitlines()
 
    if not rows:
        return None
 
    size = len(rows)
    for row in rows:
        if len(row) != size:
            return None
 
    return rows
 
 
def find_pieces(rows):
    """Locate every King and every other piece on the board."""
    kings = []
    pieces = []
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell not in PIECES:
                continue
            if cell == "K":
                kings.append((r, c))
            else:
                pieces.append((r, c, cell))
 
    return kings, pieces
 
 
def path_is_clear(rows, r1, c1, r2, c2):
    """Check every square strictly between two aligned points is empty.
    The two points must already be known to be aligned horizontally,
    vertically, or diagonally.
    """
    dr = (r2 > r1) - (r2 < r1)
    dc = (c2 > c1) - (c2 < c1)
    r, c = r1 + dr, c1 + dc
    while (r, c) != (r2, c2):
        if rows[r][c] in PIECES:
            return False
        r += dr
        c += dc
 
    return True
 
def can_attack(rows, piece_r, piece_c, piece, king_r, king_c):
    """Check whether the given piece threatens the King's square."""
    dr = king_r - piece_r
    dc = king_c - piece_c
 
    if piece == "P":
        return dr == -1 and abs(dc) == 1
    if piece == "R":
        if dr != 0 and dc != 0:
            return False
        return path_is_clear(rows, piece_r, piece_c, king_r, king_c)

    if piece == "B":
        if dr == 0 or abs(dr) != abs(dc):
            return False
        return path_is_clear(rows, piece_r, piece_c, king_r, king_c)
 
    if piece == "Q":
        if dr == 0 or dc == 0 or abs(dr) == abs(dc):
            return path_is_clear(rows, piece_r, piece_c, king_r, king_c)
        return False
 
    return False
 
 
def evaluate_board(board):
    """Return "Success", "Fail", or "Error" for the given board string.
    Never raises: any undefined/invalid input results in "Error".
    This is the reusable core, shared by checkmate() (ex00, one board,
    prints directly) and main.py in ex01 (many boards read from files,
    printed one per file).
    """
    try:
        rows = parse_board(board)
        if rows is None:
            return "Error"
        kings, pieces = find_pieces(rows)
        if len(kings) != 1:
            return "Error"
        king_r, king_c = kings[0]
 
        for (r, c, piece) in pieces:
            if can_attack(rows, r, c, piece, king_r, king_c):
                return "Success"

        return "Fail"
 
    except Exception:
        return "Error"
 
 
def checkmate(board):
    """Print "Success" if the King is in check, "Fail" otherwise.
    Never raises: any undefined/invalid input results in "Error" being
    printed and control being handed back to the caller.
    """
    print(evaluate_board(board))
 