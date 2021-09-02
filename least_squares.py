import numpy as np

# Code copied from Professor Kennedy's lecture with Sphinx-style documentation added.


def _backsolve(matrix_XTX, matrix_XTY):
    """Performs backsolving step of Gaussian elimination.

    Args:
        matrix_XTX (numpy.ndarray): The matrix representing X values of
            a linear system.
        matrix_XTY (numpy.ndarray): The matrix representing Y values of
            a linear system.

    Returns:
        numpy.ndarray: The solution matrix containing the coefficients of
        the line.
    """
    num_rows, _ = matrix_XTX.shape

    for i in reversed(range(1, num_rows)):
        for j in reversed(range(0, i)):
            s = matrix_XTX[j, i]

            matrix_XTX[j, i] -= (s * matrix_XTX[i, i])
            matrix_XTY[j] -= (s * matrix_XTY[i])

    return matrix_XTY


def solve_matrix(matrix_XTX, matrix_XTY):
    """Solves a system of linear equations for coefficients of a line.

    Args:
        matrix_XTX (numpy.ndarray): The matrix representing X values of
            a linear system.
        matrix_XTY (numpy.ndarray): The matrix representing Y values of
            a linear system.

    Returns:
        numpy.ndarray: The solution matrix containing the polynomial
            coefficients.
    """
    # Get the dimensions of the XTX matrix
    num_rows, num_columns = matrix_XTX.shape

    for i in range(0, num_rows):
        # Find column with largest entry
        largest_idx = i
        current_col = i
        for j in range(i + 1, num_rows):
            if matrix_XTX[largest_idx, current_col] < matrix_XTX[j, current_col]:
                largest_idx = j

        # Swap
        if largest_idx != current_col:
            matrix_XTX[[i, largest_idx], :] = matrix_XTX[[largest_idx, i], :]
            matrix_XTY[[i, largest_idx]] = matrix_XTY[[largest_idx, i]]

        # Scale
        scaling_factor = matrix_XTX[i, i]
        matrix_XTX[i, :] /= scaling_factor
        matrix_XTY[i] /= scaling_factor

        # Eliminate
        for row_i in range(i + 1, num_rows):
            s = matrix_XTX[row_i][i]

            matrix_XTX[row_i] = matrix_XTX[row_i] - s * matrix_XTX[i]
            matrix_XTY[row_i] = matrix_XTY[row_i] - s * matrix_XTY[i]

    _backsolve(matrix_XTX, matrix_XTY)

    return matrix_XTY


def print_matrices(matrix_XTX, matrix_XTY):
    """Prints two matrices for debugging output.

    Args:
        matrix_XTX (numpy.ndarray): A numpy ndarray representation of a matrix.
        matrix_XTY (numpy.ndarray): A numpy ndarray representation of a matrix.
    """
    print("{:*^40}".format("XTX"))
    print(matrix_XTX)

    print()
    print("{:*^40}".format("XTY"))
    print(matrix_XTY)


def create_matrix_X_and_Y_from_points(points, poly_degree=2):
    """Creates two matrices, matrix_X and matrix_Y, represenging a
    system of linear equations.

    Args:
        points (list): A list of tuples containing x and y values for the
            linear system being solved.
        poly_degree (int, optional): The degree of the polynomial to use
            when solving the linear system. Defaults to 2.

    Returns:
        tuple: A tuple containing matrix_X and matrix_Y as numpy.ndarrays
    """

    num_basis_functions = poly_degree + 1
    num_cols = num_basis_functions
    num_rows = len(points)

    matrix_X = []
    for x, y in points:
        matrix_X.append([x**n for n in range(0, num_cols)])

    matrix_Y = [y for _, y in points]

    return np.array(matrix_X), np.array(matrix_Y)


def main():
    """Main function, for testing purposes.
    """
    # Set up input data points X, Y, and XT
    # points = [(0., 0.), (1., 1.), (2., 4.)]
    # points = [(0., 61.), (30., 80.)]
    points = [(-2., 4.), (0., -2.), (2, 4)]

    # phi_hat is a polynomial of degree 2
    matrix_X, matrix_Y = create_matrix_X_and_Y_from_points(points, 1)
    print_matrices(matrix_X, matrix_Y)
    matrix_XT = matrix_X.transpose()

    # Compute XTX and XTY
    matrix_XTX = np.matmul(matrix_XT, matrix_X)
    matrix_XTY = np.matmul(matrix_XT, matrix_Y)

    print_matrices(matrix_XTX, matrix_XTY)
    print()
    print("{:-^40}".format("Solution"))
    solution = solve_matrix(matrix_XTX, matrix_XTY)
    print(solution)


if __name__ == "__main__":
    main()
