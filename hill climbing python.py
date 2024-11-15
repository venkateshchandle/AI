import random
print("name: Venkatesh Chandle, USN: 1BM22CS325")
def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def generate_initial_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

def hill_climbing(n):
    current_state = generate_initial_state(n)
    current_conflicts = calculate_conflicts(current_state)

    while current_conflicts > 0:
        neighbors = []
        for col in range(n):
            for row in range(n):
                if row != current_state[col]:
                    neighbor = current_state[:]
                    neighbor[col] = row
                    neighbors.append(neighbor)

        best_neighbor = None
        best_conflicts = current_conflicts
        for neighbor in neighbors:
            conflicts = calculate_conflicts(neighbor)
            if conflicts < best_conflicts:
                best_conflicts = conflicts
                best_neighbor = neighbor

        if best_conflicts == current_conflicts:
            return None

        current_state = best_neighbor
        current_conflicts = best_conflicts

    return current_state

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))

n = 4
solution = hill_climbing(n)

if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found (local minimum reached).")
