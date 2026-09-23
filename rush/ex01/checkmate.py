def checkmate(board):
    board = board.splitlines()
    size = len(board)

    king_row = -1
    king_col = -1

    for row in range(size):
        for col in range(len(board[row])):
            if board[row][col] == "K":
                king_row = row
                king_col = col
                break

    if king_row == -1:
        return False

    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (-1, -1), (-1, 1),
        (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < len(board[row]):
            piece = board[row][col]

            if piece != ".":
                if dr == 0 or dc == 0:
                    if piece in "RQ":
                        return True
                else:
                    if piece in "BQ":
                        return True
                break

            row += dr
            col += dc

    # Pawn
    for row, col in [
        (king_row + 1, king_col - 1),
        (king_row + 1, king_col + 1)
    ]:
        if 0 <= row < size and 0 <= col < len(board[row]):
            if board[row][col] == "P":
                return True

    return False