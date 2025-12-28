import tkinter as tk
import time
import threading

_last_popup_time = {}

def show_critical_popup(title, message, duration=10, cooldown=60):
    now = time.time()
    key = title

    if key in _last_popup_time and (now - _last_popup_time[key]) < cooldown:
        return
    _last_popup_time[key] = now

    def popup():
        
        root = tk.Tk()
        root.title(title)
        root.attributes('-topmost', True)
        root.geometry("600x180+500+300")
        root.resizable(False, False)

        label = tk.Label(root, text=message, font=('Helvetica', 13), padx=20, pady=20)
        label.pack()

        root.after(duration*1000, root.destroy)
        root.mainloop()

    threading.Thread(target=popup).start()