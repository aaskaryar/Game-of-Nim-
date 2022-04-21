# for x in range(1,6):
#     print(x)
board = [0, 2, 7, 1]
len_board = len(board)
# print(len_board)
# print(board[])
moves = []

# for y in board:
#     # print(y)
#
#     for index in range(1,len(board)):
#         value = board[index]
#         print(index, value)
        # moves.append((z,index))
# print(moves)

# [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1)]
for index in range(len(board)):
    value = board[index]
    for ele in range(1, value + 1):
        moves.append((index, ele))
print(moves)
