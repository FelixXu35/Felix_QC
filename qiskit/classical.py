"""
classical algorithms
"""

import random
from qiskit.transpiler import CouplingMap

## developed during qiskit hackathon WoQ 2023
def find_sub_group(coupling_map: CouplingMap, color: bool = False):
    """
    Automatically decide the sequence of applying XY mixers
    """
    # Initialize the step of each edge to None
    steps = {edge: None for edge in coupling_map}
    # Sort the coupling_map by their first node
    sorted_coupling_map = sorted(coupling_map)
    # Assign steps
    for edge in sorted_coupling_map:
        # Find the steps of the adjacent coupling_map
        adjacent_steps = {steps[e] for e in sorted_coupling_map if e != edge and (e[0] == edge[0] or e[1] == edge[0] or e[0] == edge[1] or e[1] == edge[1])}
        # Assign the smallest step that is not in adjacent_steps
        step = 0
        while step in adjacent_steps:
            step += 1
        steps[edge] = step
    # The number of steps is the maximum step plus one
    num_steps = max(steps.values()) + 1
    grouped_map = [[] for i in range(num_steps)]
    for edge, step in steps.items():
        grouped_map[step].append(edge)
    color_list = []
    c = [[random.random() for i in range(4)] for j in range(num_steps)]
    for edge in coupling_map:
        color_list.append(c[steps[edge]])
    if color == False:
        return grouped_map
    if color == True:
        return grouped_map, color_list