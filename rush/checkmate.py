def checkmate(board):
    list_board = board.split('\n')
    table = [row for row in list_board if row != ""]
    
    # 1. เช็กตารางว่าง
    if not table:
        print("Fail")
        return

    # 2. เช็กว่าเป็นสี่เหลี่ยมจัตุรัสหรือไม่ (Square Board)
    size = len(table)
    for row in table:
        if len(row) != size:
            print("Fail")
            return

    # 3. ค้นหาตำแหน่ง King และเช็กว่ามี King เพียงตัวเดียวหรือไม่
    king_r = None
    king_c = None
    king_count = 0
    Position_king = []
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "K":
                king_r = i
                king_c = j
                Position_king = [i, j]
                king_count += 1

    if king_count != 1:
        print("Fail")
        return

    # find other for kill king 

    Pawn = []
    Bishop = []
    Rook = []
    Queen = []

    for i in range(len(table)):
        for j in range(len(table[i])):
            piece = table[i][j]
            if piece == "P":
                Pawn.append([i, j])
            elif piece == "B":
                Bishop.append([i, j])
            elif piece == "R":
                Rook.append([i, j])
            elif piece == "Q":
                Queen.append([i, j])

    # I ja kill King
    
    # 1. Check Pawn
    if Pawn:
        for Position in Pawn:
            p_r, p_c = Position[0], Position[1]
            # Pawn เดินขึ้นด้านบน (row ลดลง) ดังนั้น King จะถูกรุกเมื่ออยู่บรรทัด p_r - 1 ในแนวเฉียง
            if king_r == p_r - 1 and (king_c == p_c - 1 or king_c == p_c + 1):
                print("Success")
                return

    # 2. Check Bishop
    if Bishop:
        for Position in Bishop:
            b_r, b_c = Position[0], Position[1]
            if abs(king_r - b_r) == abs(king_c - b_c):
                step_r = 1 if king_r > b_r else -1
                step_c = 1 if king_c > b_c else -1
                r, c = b_r + step_r, b_c + step_c
                blocked = False
                
                # แก้ไขเงื่อนไขการวนลูปจนกว่าจะถึงตำแหน่ง King
                while (r, c) != (king_r, king_c):
                    if table[r][c] not in ('.', ' '):
                        blocked = True
                        break
                    r += step_r
                    c += step_c
                if not blocked:
                    print("Success")
                    return

    # 3. Check Rook
    if Rook:
        for Position in Rook:
            r_r, r_c = Position[0], Position[1]
            if king_r == r_r or king_c == r_c:
                step_r = 0 if king_r == r_r else (1 if king_r > r_r else -1)
                step_c = 0 if king_c == r_c else (1 if king_c > r_c else -1)
                r, c = r_r + step_r, r_c + step_c
                blocked = False
                
                while (r, c) != (king_r, king_c):
                    if table[r][c] not in ('.', ' '):
                        blocked = True
                        break
                    r += step_r
                    c += step_c
                if not blocked:
                    print("Success")
                    return

    # 4. Check Queen
    if Queen:
        for Position in Queen:
            q_r, q_c = Position[0], Position[1]
            is_diagonal = abs(king_r - q_r) == abs(king_c - q_c)
            is_straight = (king_r == q_r or king_c == q_c)
            if is_diagonal or is_straight:
                step_r = 0 if king_r == q_r else (1 if king_r > q_r else -1)
                step_c = 0 if king_c == q_c else (1 if king_c > q_c else -1)
                r, c = q_r + step_r, q_c + step_c
                blocked = False
                
                while (r, c) != (king_r, king_c):
                    if table[r][c] not in ('.', ' '):
                        blocked = True
                        break
                    r += step_r
                    c += step_c
                if not blocked:
                    print("Success")
                    return

    print("Fail")