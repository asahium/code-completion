import random

def __choose_state(state_map):
    choice = random.random()
    probability_reached = 0
    for state, probability in state_map.items():
        probability_reached += probability
        if probability_reached > choice:
            return state
    return None

def next_state(chain, current_state):
    next_state_map = chain.get(current_state)
    return __choose_state(next_state_map)

def iterating_markov_chain(chain, state):
    while True:
        state = next_state(chain, state)
        yield state
