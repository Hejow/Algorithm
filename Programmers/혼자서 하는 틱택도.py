def solution(board):
    #answer = -1
    oCnt, xCnt = 0, 0
    olCnt, xlCnt = 0, 0

    for i in board:
        oCnt += i.count("O")
        xCnt += i.count("X")

    if(oCnt < xCnt):
        return 0
    if(oCnt > xCnt + 1):
        return 0

    for i in range(3):
        if (board[i] == "OOO"):
            olCnt += 1
        elif(board[i] == "XXX"):
            xlCnt += 1

        if(board[0][i] == "O" and board[1][i] == "O" and
           board[2][i] == "O"):
            olCnt += 1
        elif(board[0][i] == "X" and board[1][i] == "X" and
           board[2][i] == "X"):
            xlCnt += 1

    for i in ["O", "X"]:
        if(board[0][0] == i and board[1][1] == i and board[2][2] == i):
            if(i =="O"):
                olCnt += 1
            else:
                xlCnt += 1
        if(board[0][2] == i and board[1][1] == i and board[2][0] == i):
            if(i =="O"):
                olCnt += 1
            else:
                xlCnt += 1
    print(olCnt, xlCnt)


    if(olCnt + xlCnt > 1):
        if(olCnt > 1 and oCnt - xCnt == 1):
            return 1
        return 0

    if(xlCnt == 1 and oCnt > xCnt):
        return 0
    if(olCnt == 1 and oCnt == xCnt):
        return 0


    return 1