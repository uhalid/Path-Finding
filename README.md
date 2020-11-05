# Path-Finding
Path-Finding GUI in Python 3.8

# Algorithms:

For now, the program uses two algorithms:

-Dijkstra

-Two variant of A* one using manhattan distance and other use euclidean distance

# Installation

You have to use python 3.8 because I'm using "Assignment expressions" ([PEP 572](https://www.python.org/dev/peps/pep-0572/))

The only addiction library that you need is pygame, the library that I'm using for the graphic.
python -m pip install pygame


Soon (when I don't feel too lazy), I'm going to release a module without the graphic part that you can use in your software.

# How it works??

Here's a video:
(Future uhalid record it and add it)

Basically by left-clicking and holding you add walls, to remove them just use right button,
if you want to move start or endpoint click and drag and it will move, pressing A will run A*, with D Dijkstra

Some extra feature I added while I was bored:
- you can increase or decrease numbers of cell scrolling middle wheel.

For choosing which heuristic use in A* you have to run the program with an addiction argument, it usually uses manhattan distance.
if you want to use euclidean "main.py --euclidean."

Addiction argument you can add are:
- "main.py --no-ui", with this all window size will be of cells; otherwise it will have two buttons for starting the different algorithms.
- "main.py --beta", it enables some functions that are in beta
