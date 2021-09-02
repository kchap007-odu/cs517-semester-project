import numpy as np
import sys
import re
import os

import least_squares as ls
import parse_text_file

SAMPLE_RATE = 30.  # Seconds
OUTPUT_DIRECTORY = "output/"  # The name of the directory


def format_output(points, solution, method):
    """Performs output formatting operations.

    Args:
        points (list): A list of tuples containing X, Y data pairs.
        solution (np.ndarray): The solution matrix.
        method (string): Type of fitting used to derive the line.

    Returns:
        string: A formatted string.
    """
    x_min = points[0][0]
    x_max = points[-1][0]
    # Convert sample time back to sample number.
    y_idx = points[0][0] / SAMPLE_RATE
    constant_term = solution[1]
    linear_term = solution[0]

    output = f"{x_min:9.0f} <= x < {x_max:9.0f}; y_{y_idx:<5.0f} = {linear_term:15.4f} + {constant_term:15.4f}x; {method}\n"

    return output


def do_piecewise_linear_interpolation(core_data, filename):
    """Performs a piecewise linear interpolation and calculates an equation
    between endpoints.

    Args:
        core_data (list): An array of core temperature data.
        filename (string): The name of the output file.
    """
    with open(filename, 'w') as f:
        for i in range(1, len(core_data)):
            points = [((i-1) * SAMPLE_RATE, core_data[i-1]),
                      (i * SAMPLE_RATE, core_data[i])]

            m_X, m_Y = ls.create_matrix_X_and_Y_from_points(points, 1)
            solution = ls.solve_matrix(m_X, m_Y)

            output = format_output(points, solution, 'interpolation')
            f.write(output)


def do_global_least_squares_approximation(core_data, filename):
    """Performs a global least-squares approximation from the input data.

    Args:
        core_data (list): A list of temperatures.
        filename (string): The name of the output file.
    """
    with open(filename, 'w') as f:

        samples = [i * SAMPLE_RATE for i in range(0, len(core_data))]
        points = [(x, y) for x, y in zip(samples, core_data)]

        m_X, m_Y = ls.create_matrix_X_and_Y_from_points(points, 1)

        m_XT = m_X.transpose()
        m_XTX = np.matmul(m_XT, m_X)
        m_XTY = np.matmul(m_XT, m_Y)
        solution = ls.solve_matrix(m_XTX, m_XTY)

        output = format_output(points, solution, 'least-squares')
        f.write(output)


def main(filename="", method="interpolation"):
    """The main function.

    Returns:
        int: 0 on normal program operation, -1 otherwise
    """
    # Validate input.
    if not filename:
        print("No data file provided. Exiting...")
        return -1
    if method not in ['interpolation', 'least-squares']:
        print(f"Unrecognized method: {method}")
        return -1

    basename = filename.split(os.path.sep)[-1]
    cores = parse_text_file.parse_text_file(filename)

    # Iterate over the list of core data.
    for n in range(0, len(cores)):
        output_name = OUTPUT_DIRECTORY + \
            basename.replace('.txt', f"-core-{n}.txt")

        if method == 'interpolation':
            do_piecewise_linear_interpolation(cores[n], output_name)
        elif method == 'least-squares':
            do_global_least_squares_approximation(cores[n], output_name)

    return 0


if __name__ == "__main__":
    if not os.path.isdir(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

    args = sys.argv[1:]
    main(*args)
