#import urllib.request
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinterhtml import HtmlFrame

root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")

frame.set_content("<html></html>")
 
#frame.set_content(urllib.request.urlopen("http://thonny.cs.ut.ee").read().decode())
#print(frame.html.cget("zoom"))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
