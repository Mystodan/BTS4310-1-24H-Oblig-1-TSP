# Description: This file contains the algorithms used to solve the TSP problem
import random
import time
from enum import Enum


class HelperFunctions:
    """Class to hold the helper functions"""

    def calculate_total_distance(self, tour: list, matrix: list) -> int:
        """Calculates the total distance of the tour"""
        return (
            sum(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            + matrix[tour[-1]][tour[0]]
        )  # Sum the distances between each city and the first city


class Algorithms:
    """Class to hold the algorithms used to solve the TSP problem"""

    class AlgorithmType(Enum):
        """Enum class for the algorithm to use"""

        RANDOM = "random"
        GREEDY = "greedy"

    class InitialAlgorithm:
        """Class to hold the initial algorithms"""

        def __init__(self):
            pass

        def random_alg(self, matrix: list) -> tuple[list, float]:
            """Randomly shuffles the cities and returns the tour"""
            start_time = time.time()
            cities = list(range(len(matrix)))
            random.shuffle(cities)
            end_time = time.time()
            return (
                cities,
                end_time - start_time,
            )  # Return the tour and the time it took to find it

        def nearest_neighbor_alg(self, matrix: list) -> tuple[list, float]:
            """Finds the nearest neighbor for each city and returns the tour"""
            start_time = time.time()
            start = random.randint(0, len(matrix) - 1)
            visited = [start]
            unvisited = [
                i for i in range(len(matrix)) if i != start
            ]  # All cities except the starting city
            current_city = start

            while unvisited:  # While there are still unvisited cities
                next_city = min(
                    unvisited, key=lambda x: matrix[current_city][x]
                )  # Find the nearest city
                visited.append(next_city)
                unvisited.remove(next_city)
                current_city = next_city  # Move to the next city
            end_time = time.time()
            return (
                visited,
                end_time - start_time,
            )  # Return the tour and the time it took to find it

    class OptimizeAlgorithm:
        """Class to hold the optimization algorithms"""

        def __init__(self):
            pass

        def two_opt(self, tour: list, matrix: list) -> tuple[list, float]:
            """Optimizes the tour using the 2-opt algorithm"""
            start_time = time.time()  # Start the timer

            def calculate_segment_distance(
                tour, matrix, start, end
            ):  # Calculate the distance of a segment of the tour
                return sum(
                    matrix[tour[i]][tour[i + 1]] for i in range(start, end)
                )  # Sum the distances between each city in the segment

            improved = True  # initialize the improved variable
            calculate_total_distance = HelperFunctions().calculate_total_distance
            best_distance = calculate_total_distance(
                tour, matrix
            )  # Calculate the initial distance of the tour

            while improved:
                improved = False  # Assume that the tour is not improved
                for i in range(1, len(tour) - 2):
                    for j in range(i + 2, len(tour)):
                        if j - i == 1:
                            continue  # Skip adjacent edges
                        new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                        new_distance = (
                            best_distance
                            - calculate_segment_distance(tour, matrix, i - 1, j)
                            + calculate_segment_distance(new_tour, matrix, i - 1, j)
                        )
                        if new_distance < best_distance:
                            tour = new_tour  # Update the tour
                            best_distance = new_distance  # Update the best distance
                            improved = True

            end_time = time.time()
            return tour, end_time - start_time
