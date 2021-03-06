from heapq import *
from Node_graph import *
from costanti import *
import math
import copy

def calculate_cost(x1, y1, x2, y2, heuristic):
    if heuristic == "MANHATTAN":
        return abs(x1-x2) + abs(y1-y2)
    elif heuristic == "EUCLIDEAN":
        return math.sqrt( (x1-x2)**2 + (y1-y2)**2)


def astar(width_matrix, height_matrix, grid, start_node, end_node, heuristic):
    if(heuristic == "MANHATTAN"):
        diagonal = False
    elif heuristic == "EUCLIDEAN":
        diagonal = True
    matrix = copy.deepcopy(grid)
    
    min_heap = []
    distance = [[-1 for k in range(width_matrix)]
                for i in range(height_matrix)]
    start_node = matrix[start_node.y][start_node.x]
    end_node = matrix[end_node.y][end_node.x]
    start_node.weight = 0
    start_node.g_cost = 0
    start_node.h_cost = calculate_cost(
        start_node.x, start_node.y, end_node.x, end_node.y, heuristic)
    heappush(min_heap, start_node)
    nodes_in_order = []
    try:
        while current:= heappop(min_heap):
                # nodes_in_order.append([])
                # print("sono in", current.x, current.y)
            distance[current.y][current.x] = current.weight

            for x_off in range(-1, 2):
                for y_off in range(-1, 2):
                    new_x = current.x + x_off
                    new_y = current.y + y_off
                    
                    if not diagonal and (abs(x_off) == abs(y_off)):
                        # print("salto ", x_off, y_off)
                        continue

                    if((x_off == 0 and y_off == 0) or not can_go(width_matrix, height_matrix, new_y, new_x)):
                        continue


                    next_node = matrix[new_y][new_x]
                    if(current.g_cost + 1 < next_node.g_cost and not next_node.type == "W"):
                        next_node.h_cost = calculate_cost(
                            next_node.x, next_node.y, end_node.x, end_node.y, heuristic)
                        next_node.g_cost = current.g_cost + 1
                        # print("da ", current.x, current.y, current.g_cost, current.h_cost,
                        #       "vado a", new_x, new_y, next_node.g_cost, next_node.h_cost)
                        next_node.weight = next_node.h_cost + next_node.g_cost
                        heappush(min_heap, next_node)
                        next_node.parent = (current.y, current.x)
                        # nodes_in_order[-1].append(next_node)
                        nodes_in_order.append(next_node)
                    if(next_node == end_node):
                        raise Exception("end")

    except Exception as ex:
        template = "tipo {0} dettagli:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    return(end_node.g_cost, nodes_in_order[:-1][:-1], matrix, start_node, end_node)


if __name__ == "__main__":
    res = astar(2, 2, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   Node(0, 0, 0), Node(0, 1, INF))
    print(res[0])
