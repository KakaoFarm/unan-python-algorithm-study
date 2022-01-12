import sys
board = sys.stdin.readline().rstrip().split('.')

ans = True
print(board)
board_l =[]
for i in board:
    if 'X' in i:
        if len(i) % 4 == 0:
            x = str(i.replace('X','A'))
            board_l.append(x)
        elif len(i) % 2 == 0:
            x = str(i[-1:-3:-1].replace('X','B'))
            x = i[:-2:1].replace('X','A') + x 
            board_l.append(x)
        else:
            ans = False
    else:
        board_l.append('.')
print(board_l)
