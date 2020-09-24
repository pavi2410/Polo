#!/usr/bin/env python3
from tkinter import Tk

import ReactiPy
from components import frame, button, label
from hooks import use_state

app = Tk()


def ui():
    count, set_count = use_state(0)

    def update_counter():
        print('test->', count())
        set_count(int(count()) + 1)

    return frame()(
        "Hello World",
        label(text='Count is ' + str(count())),
        button(text="Click Me", padding=8, width=16, on_click=lambda: update_counter())
    )


ReactiPy.render(ui, app)
app.geometry()
app.mainloop()
