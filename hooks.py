state_registry = {}


def gen_state_counter():
    i = -1
    while True:
        i += 1
        yield i


state_counter = gen_state_counter()


def use_state(init):
    name = 'state_' + str(next(state_counter))

    def get_state():
        return state_registry[name]

    def set_state(v):
        state_registry[name] = v

    set_state(init)
    return get_state, set_state
