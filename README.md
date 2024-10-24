# BTS4310-1-24H-Oblig-1-TSP
By Daniel Hao Huynh
In this assignment , we are going to solve the travelling salesman problem.
This implementation has implemented threading, meaning that after the city is generated, all the algorithms run concurrently.
### TSP
This problem is NP- hard, in computational complexity theory, NP-Hardness is used to classify problems that are, in a sense, as hard as the hardest problems in NP (nondeterministic polynomial time)
We are going to use the nearest neighbor heuristic algorithm as our greedy initial algorithm
### Random algorithm for TSP
Well this algorithm just randomizes the matrix inputted and outputs a random tour.
### Nearest Neighbor Heuristic for TSP
The Nearest Neighbor heuristic for TSP is a greedy algorithm that builds a tour by repeatedly visiting the nearest unvisited city until all cities have been visited. Here's a breakdown of how it works:

1. Start at a Random City: Select a random starting city.
2. Initialize Visited and Unvisited Lists: Keep track of visited and unvisited cities.
3. Find the Nearest Unvisited City: From the current city, find the nearest unvisited city and move to it.
4. Repeat Until All Cities are Visited: Continue the process until all cities have been visited.
5. Return the Tour and Time Taken: Return the sequence of visited cities (the tour) and the time taken to compute it.

### Results
This is the results after running the code with theese settings:
```py
# Constants
TESTS = (
    1000,
    3000,
    5000,
)  # Test the algorithms with city matrices of size 1000x1000, 3000x3000, and 5000x5000
DISTANCE_MAX_VALUE = 1000  # The maximum distance between two cities in the city matrix
MAX_SHOW_TOUR_LENGTH = 3  # The maximum number of cities to show in the tour before setting show_tours to False in outprint()

```
1. 1000 Tours
```
time elapsed to solve using a basic random algorithm: 
        0.0 seconds
time to optimize:
        657.702832698822 seconds
total time elapsed:
        657.702832698822 seconds
old distance:
        1973
new distance:
        1000
time elapsed to solve using a basic greedy algorithm: 
        0.1880350112915039 seconds
time to optimize:
        446.1343762874603 seconds
total time elapsed:
        446.32241129875183 seconds
old distance:
        1002
new distance:
        1000
```
3. 3000 Tours
```
time elapsed to solve using a basic random algorithm: 
        0.0010035037994384766 seconds
time to optimize:
        7733.079829454422 seconds
total time elapsed:
        7733.080832958221 seconds
old distance:
        6049
new distance:
        3002
time elapsed to solve using a basic greedy algorithm: 
        1.40675950050354 seconds
time to optimize:
        7153.289403915405 seconds
total time elapsed:
        7154.696163415909 seconds
old distance:
        3002
new distance:
        3000
```
5. 5000 Tours  
```
time elapsed to solve using a basic random algorithm:
        0.0010035037994384766 seconds
time to optimize:
        24925.62091612816 seconds
total time elapsed:
        24925.621919631958 seconds
old distance:
        9992
new distance:
        5001
time elapsed to solve using a basic greedy algorithm:
        1.9668128490447998 seconds
time to optimize:
        16849.462002277374 seconds
total time elapsed:
        16851.42881512642 seconds
old distance:
        5003
new distance:
        5000
```
<br>After running the code with 1000x1000, 3000x3000, and 5000x5000 cities, it should be apparant that the time taken to run each test increase significantly, this is due to the complexity of the problem being run multiple times. In 5000x5000 using the greedy algorithm already comes close to the optimal solution, however in order to find the optimal solution, the time elapsed is significantly increased:
- 1000x1000 -> 3000x3000 -> 5000x5000
- 7.43870685 minutes (446.32241129875183 seconds) -> 1.9874156 hours (7154.696163415909 seconds) -> 4.68095245 hours (16851.42881512642)

<br>This means that the time has increased:
- from 1000x1000 -> 3000x3000 increase by 1.86343715 hours
- from 3000x3000 -> 5000x5000 increase by 2.69353685 hours
<br>And this is with threading.

### Running the file

Using this command in the terminal from root would run the file
```sh
python .\tsp.py   
```


