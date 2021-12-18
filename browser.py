try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from cefpython3 import cefpython as cef

root = tk.Tk()
app = MainFrame(root)
cef.Initialize()
app.mainloop()
print("exited mainloop")
cef.Shutdown()

class Mainframe(tk.Frame);
    def __init__(self, root):
        root.geometry("900x640")
        tk.Frame.__init__(self, root)
        self.master.title("webbrowser")
        self.navigation_bar = NavigationBar(self)
        self.browser_frame = BrowserFrame(self, self.navigation_bar)
