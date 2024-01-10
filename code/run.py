# Search methods

import search
from collections import namedtuple
import time

Algorithm = namedtuple("Algorithm", "name func")

PRINT_IN_TERMINAL = True

REPEAT = 100

algorithms = [
    Algorithm("BREADTH", search.breadth_first_graph_search),
    Algorithm("DEPTH", search.depth_first_graph_search),
    Algorithm("B&B", search.branch_and_bound_search),
    Algorithm("B&B WITH SUBESTIMATION", search.branch_and_bound_search_with_subestimation)
]

PROBLEMS = [
    ["A", "B"],
    ["O", "E"],
    ["G", "Z"],
    ["N", "D"],
    ["M", "F"]
]

times = [0 for _ in algorithms]


def test_search(func, title):
    if PRINT_IN_TERMINAL: print(f"\n\t# {title}")
    temp = time.perf_counter_ns()

    for _ in range(1, REPEAT): func(False)

    node = func(PRINT_IN_TERMINAL)

    temp = (time.perf_counter_ns() - temp) * 0.001 / REPEAT

    # if PRINT_IN_TERMINAL: print("\n\tExecution time: ", temp, "ps")
    if PRINT_IN_TERMINAL: print("\tTotal cost: ", node.path_cost, "-", node.path())

    return temp


def test_problem(problem, title):
    if PRINT_IN_TERMINAL: print(f"# {title} ***************************************************************************")
    for i in range(0, len(algorithms)):
        times[i] *= test_search(lambda show: algorithms[i].func(problem, show), algorithms[i].name)
    if PRINT_IN_TERMINAL: print()


if PRINT_IN_TERMINAL: print()

for elements in PROBLEMS:
    test_problem(search.GPSProblem(elements[0], elements[1], search.romania), f"{elements[0]}-{elements[1]}")

for index in range(0, len(times)): times[index] / len(PROBLEMS)
