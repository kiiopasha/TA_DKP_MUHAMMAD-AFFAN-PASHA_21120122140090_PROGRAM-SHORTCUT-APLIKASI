import tkinter as tk
from tkinter import Image, filedialog, Text, font
from tkinter import *
import os
from tkinter.constants import X

root=tk.Tk()
root.title('Shortcut App')

apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split (',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", ".exe"), ("all files", ".*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app, bg="white")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

canvas=tk.Canvas(root, height=500, width=700, bg="#C5B358")
canvas.pack()

frame=tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.1)

openFile=tk.Button (root, text="Open File", padx=20, pady=5, fg="black", bg="#C5B358", command=addApp)
openFile.pack()

runApp=tk.Button (root, text="Run App", padx=20, pady=5, fg="black", bg="#C5B358", command=runApps)
runApp.pack()

labelmain=tk.Label (frame, text="Current App Selected\n", font="bold", fg="black", bg="white")
labelmain.pack()

class closeProgram:
    def __init__(self, main):
        closeFrame=tk.Frame(main)
        closeFrame.pack()
        
        self.button=tk.Button(main, text="Close Program", padx=20, pady=5, bg="#C5B358", command=root.destroy)
        self.button.pack()

e=closeProgram(root)


for app in apps:
    label=tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')