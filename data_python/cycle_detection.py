from enum import Enum


class TraversalState(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

def is_in_cycle(graph, traversal_states, vertex):
    if traversal_states[vertex] == TraversalState.GRAY:
        return True
    traversal_states[vertex] = TraversalState.GRAY
    for neighbor in graph[vertex]:
        if is_in_cycle(graph, traversal_states, neighbor):
            return True
    traversal_states[vertex] = TraversalState.BLACK
    return False


def contains_cycle(graph):
    traversal_states = {vertex: TraversalState.WHITE for vertex in graph}
    for vertex, state in traversal_states.items():
        if (state == TraversalState.WHITE and
           is_in_cycle(graph, traversal_states, vertex)):
            return True
    return False
