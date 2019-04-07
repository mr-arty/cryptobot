from pyredux import create_store
from copy import deepcopy


def app_reducer_sr(state, action):
    if action['type'] == 'SET_S1':
        new_state = deepcopy(state)
        new_state['action'] = action['support_1']
        return new_state
    elif action['type'] == 'SET_S2':
        new_state = deepcopy(state)
        new_state['action'] = action['support_2']
        return new_state
    elif action['type'] == 'SET_R1':
        new_state = deepcopy(state)
        new_state['action'] = action['resistance_1']
        return new_state
    elif action['type'] == 'SET_R2':
        new_state = deepcopy(state)
        new_state['action'] = action['resistance_2']
        return new_state
    return state

# store.dispatch(({'type': 'SET_S1', 'support_1': 's1'}))


def app_reducer_pos(state, action, pos):
    if action['type'] == 'increase_pos':
        return state.copy(total_pos=state.total_pos + pos)
    elif action['type'] == 'decrease_pos':
        return state.copy(total_pos=state.total_pos - pos)

    return state

store = create_store(app_reducer_sr,  {})

#store_pos = create_store(app_reducer_pos)