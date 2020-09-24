from ReactiPy import create_element


def frame(**props):
    return lambda *children: create_element('frame', props, *children)


def label(**props):
    return create_element('label', props)


def button(**props):
    return create_element('button', props)
