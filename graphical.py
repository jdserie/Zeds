"""Desktop storybook for the original branching scenario."""
import tkinter as tk
from tkinter import ttk


def play_graphical(scenes, scene_text):
    root = tk.Tk()
    root.title('Zeds')
    root.minsize(445, 365)
    art = tk.Canvas(root, height=116, background='#142731', highlightthickness=0)
    art.pack(fill='x')
    art.create_oval(28, 18, 101, 91, fill='#e08058', outline='')
    for left, width, height in [(14, 22, 36), (41, 22, 55), (76, 25, 38), (107, 24, 62), (136, 28, 42)]:
        art.create_rectangle(left, 116 - height, left + width, 116, fill='#263f49', outline='')
    art.create_text(175, 56, text='ZEDS', anchor='w', fill='#f6e8ca', font=('TkDefaultFont', 34, 'bold'))

    panel = ttk.Frame(root, padding=18)
    panel.pack(fill='both', expand=True)
    ttk.Label(panel, text='Your name').pack(anchor='w')
    player = tk.StringVar()
    ttk.Entry(panel, textvariable=player).pack(fill='x', pady=(2, 10))
    title = ttk.Label(panel, font=('TkDefaultFont', 16, 'bold'))
    title.pack(anchor='w')
    body = ttk.Label(panel, wraplength=400, justify='left')
    body.pack(anchor='w', pady=(5, 12))
    controls = ttk.Frame(panel)
    controls.pack(fill='x')
    scene = scenes['start']

    def show(key):
        nonlocal scene
        scene = scenes[key]
        title.configure(text=scene.title)
        render_text()
        for widget in controls.winfo_children():
            widget.destroy()
        for label, target in scene.choices or (('Play again', 'start'),):
            ttk.Button(controls, text=label, command=lambda next_scene=target: show(next_scene)).pack(side='left', padx=(0, 8))

    def render_text(*args):
        body.configure(text=scene_text(scene, player.get()))

    player.trace_add('write', render_text)
    show('start')
    root.mainloop()
