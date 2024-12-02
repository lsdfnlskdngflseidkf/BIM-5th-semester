# Function to generate neighbors
def generate_neighbors(x, step=0.1, lower=0, upper=4):
    # Generate neighbors by moving up or down by step size, staying within bounds
    return [x + step, x - step]

# Hill Climbing algorithm
def hill_climbing(f, x0):
    x = x0  # Start with the initial solution
    while True:
        neighbors = generate_neighbors(x)  # Generate neighbors of x
        best_neighbor = max(neighbors, key=f)  # Pick the best neighbor
        if f(best_neighbor) <= f(x):  # Stop if no improvement
            return x
        x = best_neighbor  # Move to the best neighbor

# Define the function to maximize
def f(x):
    return -x**2 + 4*x  # Example function: f(x) = -x^2 + 4x

# Main program
if __name__ == "__main__":
    initial_solution = 0  # Starting point for the search
    best_x = hill_climbing(f, initial_solution)
    print(f"Best x: {best_x}, f(x): {f(best_x)}")
