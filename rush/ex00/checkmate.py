def checkmate(board):
    rows = board.splitlines()
    size = len(rows)

    king_row = -1
    king_col = -1

    for r in range(size):
        for c in range(len(rows[r])):
            if rows[r][c] == "K":
                king_row = r
                king_col = c

    if king_row == -1:
        return

    # Rook / Queen
    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (-1, -1), (-1, 1),
        (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < len(rows[r]):
            piece = rows[r][c]

            if piece != ".":
                if dr == 0 or dc == 0:
                    if piece == "R" or piece == "Q":
                        print("Success")
                        return
                else:
                    if piece == "B" or piece == "Q":
                        print("Success")
                        return
                break

            r += dr
            c += dc

    # Pawn
    for r, c in [
        (king_row + 1, king_col - 1),
        (king_row + 1, king_col + 1)
    ]:
        if 0 <= r < size and 0 <= c < len(rows[r]):
            if rows[r][c] == "P":
                print("Success")
                return

    print("Fail")