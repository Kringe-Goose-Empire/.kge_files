from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys

Tk().withdraw()
filename = askopenfilename()
if not filename.endswith('.kge'):
    sys.exit()
file = open(filename, "r")

import tkinter as tk
window = tk.Toplevel()
window.title(str(filename))
from PIL import Image, ImageTk
import requests, urllib
width=512
window.minsize(width, 128)


i=0
varibles = []
while True:
    line = file.readline()
    if not line:
        break
    if(line[0]=="#"):
        continue
    i+=1
    if("end" in line):
        break
    if("imgi" in line):
        line = line.replace('imgi ','') 
        line = line.replace('\n','') 
        #print(line)
        #varibles[i]=line
        urllib.request.urlretrieve(line, "pickture.png")
        image = Image.open(r"pickture.png")
        size = 128, 128
        image = image.resize(size)
        image = ImageTk.PhotoImage(image)
        varibles.append(image)
        tk.Label(window, image = image).grid(column=0, row=i)  
        #del image
        window.update()
        continue
    if("img" in line):
        line = line.replace('img ','') 
        line = line.replace('\n','') 
        #print(line)
        #varibles[i]=line
        image = Image.open(line)
        size = 128, 128
        image = image.resize(size)
        image = ImageTk.PhotoImage(image)
        varibles.append(image)
        tk.Label(window, image = image).grid(column=0, row=i)    
        #del image
        window.update()
        continue  
    tk.Label(window, text=line.strip()).grid(column=0, row=i)  
    window.update()
file.close()
#while True: window.update()
#del image
#print(varibles)

def on_destroy(event):
    if event.widget != window:
        return
    sys.exit()

window.bind("<Destroy>", on_destroy)
window.mainloop()
sys.exit()