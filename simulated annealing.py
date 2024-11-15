import random
import math
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

def get_neighbors(board):
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if row != board[col]:
                neighbor = board[:]
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing(n, initial_temperature, cooling_rate):
    current_state = generate_initial_state(n)
    current_cost = calculate_conflicts(current_state)
    temperature = initial_temperature

    while current_cost > 0 and temperature > 0:
        neighbors = get_neighbors(current_state)
        next_state = random.choice(neighbors)
        next_cost = calculate_conflicts(next_state)

        if acceptance_probability(current_cost, next_cost, temperature) > random.random():
            current_state = next_state
            current_cost = next_cost

        temperature *= cooling_rate

    if current_cost == 0:
        return current_state
    else:
        return None

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))

n = 4
initial_temperature = 1000
cooling_rate = 0.99
solution = simulated_annealing(n, initial_temperature, cooling_rate)

if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found.")
