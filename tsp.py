"""This module contains the main function for the TSP assignment"""

import threading
import random
import numpy as np
from algorithms import Algorithms, HelperFunctions

# Constants
TESTS = (
    500,
)  # Test the algorithms with city matrices of size 1000x1000, 3000x3000, and 5000x5000
DISTANCE_MAX_VALUE = 1000  # The maximum distance between two cities in the city matrix
MAX_SHOW_TOUR_LENGTH = 10  # The maximum number of cities to show in the tour before setting show_tours to False in outprint()


def outprint(
    init_tour,
    opt_tour,
    city,
    name,
    init_time,
    opt_time,
    show_tours=False,
    show_time=False,
) -> str:
    """Formats and prints the output of the algorithm"""
    act_print = ""
    calculate_total_distance = HelperFunctions().calculate_total_distance
    init_print, opt_print = (
        f"initial {name} {init_tour},",
        f"optimized {name} tour: {opt_tour},",
    )
    time_print = f"time elapsed to solve using a basic {name} algorithm: \n\t{init_time}\ntime to optimize: \n\t{opt_time}\ntotal time elapsed: \n\t{init_time+opt_time}\nold distance: \n\t{calculate_total_distance(init_tour,city)}\nnew distance: \n\t{calculate_total_distance(opt_tour,city)}\n"
    act_print += f"Calculating the shortest path for a {len(city)} city tour using a {name} algorithm\n"
    var = (
        (init_print + " " + opt_print + " ")
        if show_tours or len(city) > MAX_SHOW_TOUR_LENGTH
        else ""
    )
    act_print += f"{var}{name} distance {calculate_total_distance(init_tour,city)} -> {calculate_total_distance(opt_tour,city)}\n"
    act_print += time_print if show_time else ""
    return act_print


def genmatrix(matrix_length: int, matrix_dist_max: int) -> list:
    """Generates a random matrix of size matrix_length x matrix_length with distance values between 1 and matrix_dist_max"""
    matrix = np.array([[_ for _ in range(matrix_length)] for _ in range(matrix_length)])

    for y in range(matrix_length):
        for x in range(matrix_length):
            matrix[x][y] = matrix[y][x] = (
                random.randint(1, matrix_dist_max) if x != y else 0
            )

    return matrix


def get_algorithm_as_func(algorithm: Algorithms.AlgorithmType) -> tuple[callable, str]:
    """Runs the initial algorithm"""
    func: None | callable = None  # Initialize the modlular function variable
    if (
        algorithm == Algorithms.AlgorithmType.RANDOM
    ):  # Set the function to the random algorithm if the algorithm is RANDOM
        func = Algorithms.InitialAlgorithm().random_alg
        init_text = algorithm.value
    else:  # Set the function to the nearest neighbor algorithm if the algorithm is GREEDY
        func = Algorithms.InitialAlgorithm().nearest_neighbor_alg
        init_text = algorithm.value

    return func, init_text


def run_algorithm(
    algorithm: Algorithms.AlgorithmType,
    import_city: None | list = None,
    show_city: bool = False,
    **matrix,
) -> tuple[list, float]:
    """Runs the algorithm and prints the output"""
    algprint = ""
    # Error handling
    if import_city is not None:  # Check if a city matrix is imported
        assert (
            "matrix_length" not in matrix and "max_dist" not in matrix
        ), "Cannot initialize city and import city at the same time"
    elif "matrix_length" in matrix and "max_dist" in matrix:
        assert (
            import_city is None
        ), "Cannot initialize Matrix and import city at the same time"
    if (
        "matrix_length" in matrix
        and "max_dist" not in matrix
        or "max_dist" in matrix
        and "matrix_length" not in matrix
    ):
        raise ValueError(
            "max_dist, and matrix_length is required if no import_city is specified"
        )
    # Getter for algorithm function and algorithm name
    func, init_text = get_algorithm_as_func(algorithm=algorithm)

    # Algorithm execution
    matrix_length, max_dist = (
        matrix["matrix_length"] if "matrix_length" in matrix else None
    ), (
        matrix["max_dist"] if "max_dist" in matrix else None
    )  # Get the matrix length and max distance from the matrix dictionary
    city = (
        genmatrix(matrix_length, max_dist) if import_city is None else import_city
    )  # Generate a random city matrix if no city
    init_tour, init_time = func(city)

    opt_tour, opt_time = Algorithms.OptimizeAlgorithm().two_opt(
        tour=init_tour, matrix=city
    )  # Optimize the tour using the 2-opt algorithm
    city_length = len(city)
    algprint += f"Running the {init_text} algorithms with a city matrix of size {city_length}x{city_length}\n"
    if show_city:
        algprint += f"City matrix: \n{city}\n"
        # Print the city matrix if show_city is True

    algprint += outprint(  # Print the output of the algorithm
        init_tour=init_tour,
        opt_tour=opt_tour,
        city=city,
        name=init_text,
        init_time=init_time,
        opt_time=opt_time,
        show_time=True,
    )
    print(algprint)


def oblig1(*args) -> None:
    """Runs the algorithms with different city matrix sizes"""

    def check_all_args(*args, comparetype=int) -> bool:
        """Checks if all arguments are of the same type"""
        for arg in args:
            if not isinstance(arg, comparetype):
                return False
        return True

    assert check_all_args(*args), "All arguments must be integers"

    def run_algorithms(arg):
        """Runs the algorithms with a city matrix of size arg x arg"""
        city = genmatrix(arg, DISTANCE_MAX_VALUE)
        run_algorithm(  # Run the random algorithm
            algorithm=Algorithms.AlgorithmType.RANDOM, import_city=city, show_city=True
        )
        run_algorithm(  # Run the greedy algorithm
            algorithm=Algorithms.AlgorithmType.GREEDY, import_city=city, show_city=True
        )

    threads = []  # Initialize the threads list
    for arg in args:
        thread = threading.Thread(
            target=run_algorithms, args=(arg,)
        )  # Create a thread for each argument
        threads.append(thread)  # Append the thread to the threads list
        thread.start()  # Start the thread

    for thread in threads:  # Loop through all threads
        thread.join()  # Wait for all threads to finish their jobs


if __name__ == "__main__":  # Run the algorithm
    oblig1(*TESTS)  # Run the algorithms with the city matrix sizes in TESTS
