import sys

def matrix_chain_order(dimensions):
    """
    Implements Matrix Chain Multiplication using Dynamic Programming.
    
    Args:
    - dimensions: A list of dimensions representing the matrices in the chain.
    
    Returns:
    - dp: A table containing the minimum number of scalar multiplications.
    - s: A table containing the optimal split point for matrix chain multiplication.
    """
    # Check if dimensions list is valid
    if not dimensions or len(dimensions) < 2:
        raise ValueError("Matrix dimensions list must contain at least two values representing matrix chains.")
    
    # Check for non-numeric dimensions
    if any(not isinstance(d, int) or d <= 0 for d in dimensions):
        raise ValueError("Matrix dimensions must be positive integers.")

    n = len(dimensions) - 1  # Number of matrices
    
    # dp[i][j] will store the minimum number of multiplications needed to multiply matrices from i to j
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # s[i][j] will store the index of the matrix after which the optimal split happens
    s = [[0 for _ in range(n)] for _ in range(n)]
    
    # l is the chain length
    for length in range(2, n + 1):  # length of the chain
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                # q = cost of multiplying matrices from i to k and from k+1 to j, plus the cost of multiplying the two results
                q = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k  # record the optimal split point

    return dp, s

def print_optimal_parenthesization(s, i, j):
    """
    Recursively prints the optimal parenthesization of the matrix chain multiplication.
    
    Args:
    - s: The table storing optimal split points.
    - i, j: The current subproblem (i-th matrix to j-th matrix).
    """
    if i == j:
        print(f"A{i+1}", end="")  # Print the matrix name (1-based index)
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])  # Left split
        print(" x ", end="")
        print_optimal_parenthesization(s, s[i][j] + 1, j)  # Right split
        print(")", end="")

# Positive Test Cases
positive_test_cases = [
    ([10, 20, 30, 40], "Test Case 1"),
    ([10, 100, 5, 50, 1], "Test Case 2 "),
    ([10, 30, 35, 15, 5, 10], "Test Case 3 "),
    ([2, 3, 4], "Test Case 4"),
    ([5, 10], "Test Case 5 "),
]

# Negative Test Cases for Invalid Matrix Dimensions
negative_test_cases = [
    ([], "Test Case 1 "),  # Empty matrix dimensions list
    (['a', 20, 30, 40], "Test Case 2 "),  # Non-numeric dimension
    ([10, -20, 30, 40], "Test Case 3 "),  # Negative dimension
    ([10, 20], "Test Case 4 "),  # Single matrix
    ([10, -100], "Test Case 5 - ")  # Inconsistent chain
]

# Running and printing output for each positive test case
print("---- Positive Test Cases ----")
for dimensions, case_name in positive_test_cases:
    print(f"\n{case_name} - Matrix Dimensions: {dimensions}")
    try:
        dp, s = matrix_chain_order(dimensions)

        # Output the minimum number of scalar multiplications
        print(f"Minimum number of scalar multiplications: {dp[0][len(dimensions) - 2]}")

        # Output the optimal parenthesization
        print("Optimal Parenthesization: ", end="")
        print_optimal_parenthesization(s, 0, len(dimensions) - 2)
        print()  # Newline at the end for better formatting
    except Exception as e:
        print(f"Error: {e}")

# Running and printing output for each negative test case
print("\n---- Negative Test Cases ----")
for dimensions, case_name in negative_test_cases:
    print(f"\n{case_name} - Matrix Dimensions: {dimensions}")
    try:
        dp, s = matrix_chain_order(dimensions)

        # Output the minimum number of scalar multiplications
        print(f"Minimum number of scalar multiplications: {dp[0][len(dimensions) - 2]}")

        # Output the optimal parenthesization
        print("Optimal Parenthesization: ", end="")
        print_optimal_parenthesization(s, 0, len(dimensions) - 2)
        print()  # Newline at the end for better formatting
    except Exception as e:
        print(f"Error: {e}")
