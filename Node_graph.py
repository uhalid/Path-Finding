from dataclasses import dataclass
from costanti import *


@dataclass
class Node:
    x: int 
    y: int 
    weight: int = INF
    type: str = "N"
    parent: tuple = (-1,-1)
    fill = lambda self: 1 if self.type == "N" else 0
    previus_type: str = "N"
    # f_cost :  INT = INF
    g_cost :  int = INF
    h_cost:  int = INF

    def __lt__(self, other):
        if(self.weight == other.weight):
            return self.h_cost < other.h_cost
        return self.weight < other.weight


def can_go(width_matrix, height_matrix, y, x):
    return (y < height_matrix and y >= 0) and (x < width_matrix and x >= 0)


def trace_back(matrix, start_node, end_node):

    nodes_in_order = []
    next_node = end_node
    while matrix[next_node.y][next_node.x] != start_node:
        parent = next_node.parent
        nodes_in_order.append(next_node)
        next_node = matrix[next_node.parent[0]][next_node.parent[1]]
        
    return nodes_in_order[1:][::-1]
