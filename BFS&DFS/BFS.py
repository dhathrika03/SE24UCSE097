from collections import deque

# Check if X has won
def check_winner(board):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for state in win_states:
        if all(board[i] == 'X' for i in state):
            return True
    return False


# Generate possible next states
def generate_children(board):
    children = []
    for i in range(9):
        if board[i] == ' ':
            new_board = board.copy()
            new_board[i] = 'X'
            children.append(new_board)
    return children


# BFS Algorithm
def bfs(initial_board):
    queue = deque([initial_board])
    visited = []
    nodes_expanded = 0

    while queue:
        board = queue.popleft()
        nodes_expanded += 1

        if check_winner(board):
            return board, nodes_expanded

        visited.append(board)

        for child in generate_children(board):
            if child not in visited:
                queue.append(child)

    return None, nodes_expanded


# Run BFS
initial_board = [' '] * 9
solution, nodes = bfs(initial_board)

print("BFS Nodes Expanded:", nodes)
print("Winning Board:", solution)