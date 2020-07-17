# Path-Finding
Path-Finding GUI in Python 3.8

# Algorithms:

For now the program is using 2 algorithms:

-Dijkstra

-2 variant of A* one using manhattan distance and other uses euclidean distance

# Installation

You have to use python 3.8 because I'm using "Assignment expressions" ([PEP 572](https://www.python.org/dev/peps/pep-0572/))

The only addiction library that you need is pygame, the library that I'm using for the graphic.
-pip install pygame


Soon (when I don't feel too lazy), I'm gonna release a module without the graphic part that you can use in your software.

# How it works??

Here's a video:
(Future uhalid record it and add it)

Basically with clicking and holding left click you add whalls, for remove them just use right button,
if you want to move start or end point click and drag and it will move, pressing A will run A*, with D dijkstra

Some extra feature I added while I was bored:
- you can increase or decrease numbers of cell scrolling middle wheel.

for choosing which heuristic use in A* you have to run the programm with an addiction argument, normally it uses manhattan distance.
if you want to use eucliden "main.py --euclidean"

Addiction argument you can add are:
- "main.py --no-ui", with this all window size will be of cells, otherwise it will have 2 buttons for starting the different algorithms.
- "main.py --beta", it enables some function that are in beta
