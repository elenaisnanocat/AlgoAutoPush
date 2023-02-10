def deleteblock(m, n, board): #높이m r  폭n c
    
    #없앨 블록 체크
    check_del = [[0]*n for _ in range(m)]
    # print(check_del)
    for r in range(m-1):
        for c in range(n-1):
            if board[r][c] == '':
                continue
            elif board[r][c] == board[r+1][c] and board[r][c] == board[r][c+1] and board[r][c] == board[r+1][c+1]:
                check_del[r][c] = 1
                check_del[r+1][c] = 1
                check_del[r][c+1] = 1
                check_del[r+1][c+1] = 1
    # print(check_del)
    #체크한 배열보고 board에서 블록 터트리고('') 삭제될 개수 카운트
    deletecnt = 0
    for r in range(m):
        for c in range(n):
            if check_del[r][c] == 1:
                board[r][c] = ''
                deletecnt += 1
                check_del[r][c] = 0
    # print(check_del)
    # print(board)
    
    return deletecnt
    
                

def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]
    
    while True:
        deleteblocks = deleteblock(m,n,board)
        if deleteblocks == 0:
            return answer
        answer += deleteblocks
    
    #왼쪽아래부터 왼쪽위 -> 오른쪽으로 빈칸 탐색
    #빈 블록자리 채움(위에서 떨어짐)
        for c in range(n):
            blankcnt = 0
            for r in range(m-1,-1,-1):
                if board[r][c] == '':
                    blankcnt += 1
                    # print(blankcnt)
                elif blankcnt > 0 :
                    board[r+blankcnt][c] = board[r][c]
                    board[r][c] = ''
                    # print(board[r][c])
 