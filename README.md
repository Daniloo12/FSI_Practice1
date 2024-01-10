# FSI First Practice
- **University**: Universidad de Las Palmas de Gran Canaria
- **Building**: Escuela de Ingeniería Informática
- **Degree**: Grado en Ciencia e Ingeniería de Datos
- **Course**: 2º year, group 18.43
- **Subject**: Fundamentos de los Sistemas Inteligentes
- **Authors**: Daniel López Correas y Nicole Ortega Ojeda

## Functionality

This practice involves programming in Python both a branch and bound method, as well as a branch and bound method with subestimation. These algorithms are intended to find the optimal path in a graph representing the connections between Romania's cities.

## Resources used
### Development enviroment
We've employed the PyCharm Development Enviroment.

## Version control system
Throughout the development process, the primary version control system utilized was Git, serving to track alterations and preserve the various verions created.

## Design
### Run.py
It contains the main code responsible for coordinating and executing all the tests. It's designed to be configurable, featuring adjustable constants at the beginning, including algorithms and problems to be checked. Any of these constants can be modified according to preferences. For algorithms and problems, simply commenting out unwanted sections would suffice to prevent their execution.

### Search.py
We modified the graph_search method to track the number of visited, generated, and expanded nodes. Additionally, we included an option to print the results for all the run tests by using the show variable.

We also added two functions: PriorityQueue and PriorityQueueWithSubestimation. These functions are responsible for calling the search function with the corresponding parameters.

### Utils.py
We created two classes to illustrate how the append and extend functions work for Branch & Bound and Branch & Bound with subestimation.

Both classes inherit from FIFOQueue because they function like a queue but with the added feature of being ordered.

In the PriorityQueue class, we sort the list by accumulated cost using the sorted function. This sorting is applied for both append and extend, although we recognize that sorting in append might not be necessary, but we believe it's not harmful.

Similarly, in the PriorityQueueWithSubestimation class, we perform the same operations, sorting by the sum of the accumulated cost and the heuristic for both append and extend methods as in Branch and Bound.

