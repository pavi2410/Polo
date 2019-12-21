import ReactiPy


def frame(**props):
    def ch(*children):
        return ReactiPy.create_element('frame', props, *children)

    return ch


def label(**props):
    return ReactiPy.create_element('label', props)


def button(**props):
    return ReactiPy.create_element('button', props)
