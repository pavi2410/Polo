from tkinter import Tk
from tkinter.ttk import Label, Button, Frame, Widget
from typing import Union


class VNode:
    def __init__(self, type_name, props=None, events=None, children=None):
        if props is None:
            props = {}
        if events is None:
            events = {}
        if children is None:
            children = []

        self.type_name = type_name
        self.props = props
        self.events = events
        self.children = children

    def __str__(self):
        return f'Node(type_name={self.type_name},props={self.props},events={self.events},children={self.children},)'


def create_text_element(text: str) -> VNode:
    return VNode('label', {'text': text})


def create_element(el_type, props=None, *children) -> VNode:
    if props is None:
        props = {}

    events = {k[3:]: v for k, v in props.items() if str.startswith(k, 'on_')}
    props = {k: v for k, v in props.items() if not str.startswith(k, 'on_')}

    assert isinstance(el_type, str)
    return VNode(el_type, props, events,
                 [child if isinstance(child, VNode) else create_text_element(child) for child in children])


def create_tk_widget(name: str, parent: Widget) -> Widget:
    if name == 'label':
        return Label(master=parent)
    elif name == 'button':
        return Button(master=parent)
    elif name == 'frame':
        return Frame(master=parent)


prop_map = {}

event_map = {
    'click': 'command'
}


def render(component, parent: Union[Tk, Widget]):
    if callable(component):
        component = component()

    tk_widget = create_tk_widget(component.type_name, parent)

    for k, v in component.props.items():
        if k in prop_map:
            k = prop_map[k]
        tk_widget[k] = v

    for k, v in component.events.items():
        if k in event_map:
            k = event_map[k]
        tk_widget[k] = v

    for child in component.children:
        render(child, tk_widget)

    tk_widget.pack()
