from tkinter.ttk import Label, Button, Frame


def create_text_element(text):
    return {
        "type": "label",
        "props": {
            "text": text
        },
        "children": []
    }


def create_element(type, props=None, *children):
    if props is None:
        props = {}
    return {
        "type": type,
        "props": {
            **props
        },
        "children": [child if isinstance(child, dict) else create_text_element(child) for child in children]
    }


def create_tk_widget(name, parent):
    if name == 'label':
        return Label(master=parent)
    elif name == 'button':
        return Button(master=parent)
    elif name == 'frame':
        return Frame(master=parent)


def render(element, container):
    tk_widget = create_tk_widget(element["type"], container)

    for k, v in element["props"].items():
        tk_widget.config(**{k: v})

    for child in element["children"]:
        render(child, tk_widget)

    tk_widget.pack()
