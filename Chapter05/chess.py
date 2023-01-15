def isValidChessBoard(dct):
    key = list(dct.keys())
    val = list(dct.values())
    if val.count('bking') == val.count('wking') != 1:
        return False
    for i in key:
        if i[0] > '8':
            return False
        elif i[1] > 'h':
            return False
    for j in val:
        if j[0] not in ["b", "w"]:
            return False
        elif j[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            return False
    return True


dct1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
ans = isValidChessBoard(dct1)
print(ans)
