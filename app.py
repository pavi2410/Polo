from tkinter import Tk

import ReactiPy
from components import frame, button

ui = frame()(
    "Hello World",
    button(text="Click Me", command=lambda: print("clicked"))
)

app = Tk()
ReactiPy.render(ui, app)
app.mainloop()
