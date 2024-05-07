from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import json

# ------ Export To Json ------
def exportToJson():

    data = {
        "name": input1.get(),
        "numberOfDuplications": input2.get(),
        "keepOldData": input3.get()
    }

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    text = input1.get()
    print(text)


# ----- Quit Sub Menu -----
def quit():
    top = Toplevel(root, pady=10, padx=10)
    top.geometry('200x100')
    top.title("Quit?")

    label = ttk.Label(top, text='Are you sure you want to quit?').grid(column=0,row=0,columnspan=2)
    ttk.Button(top, text="Quit", command=root.destroy).grid(column=0, row=1, pady=(30,0))
    ttk.Button(top, text="Cancel", command=top.destroy).grid(column=1, row=1, pady=(30,0))

# Create root, frame, and grid
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
root.title('JSON Settings Editor')

# ------ Title ------
label = ttk.Label(frm, text="JSON Settings Editor",font=("Arial", 20) ).grid(column=0,row=1,columnspan=2)

# -----  Logo  ------
imageFile = Image.open('./logo.png')


# ----- Image ------
image = ImageTk.PhotoImage(imageFile.resize((100, 100)))
icon = Label(frm, image=image)
icon.image = image
icon.grid(column=0, row=3, pady=(0,50),columnspan=2)

label = ttk.Label(frm, text="Settings", font=("Arial", 16) ).grid(column=0,row=4,columnspan=2)

label = ttk.Label(frm, text='Fill out the settings below and then click "Export To JSON"').grid(column=0,row=5,columnspan=2)
label = ttk.Label(frm, text='to export the settings for your program.').grid(column=0,row=6,columnspan=2, pady=(0, 20))


# ----- Inputs ------
ttk.Label(frm, text="Name", justify="left", anchor="w").grid(column=0, row=10, sticky = W)
input1 = ttk.Entry(frm)
input1.grid(column=1, row= 10)

ttk.Label(frm, text="Number Of Duplications", justify="left", anchor="w").grid(column=0, row=12, padx= (0,10), sticky = W)
input2 = ttk.Entry(frm)
input2.grid(column=1, row= 12)

ttk.Label(frm, text="Keep Old Data?", justify="left", anchor="w").grid(column=0, row=14, sticky = W)
input3 = ttk.Entry(frm)
input3.grid(column=1, row= 14)



# ----- Export -----
ttk.Button(frm, text="Export To JSON", command=lambda: exportToJson()).grid(column=0, row=99, columnspan=1, pady=(30,0))


# Quit Button
ttk.Button(frm, text="Quit", command=lambda: quit()).grid(column=1, row=99,columnspan=2, pady=(30,0))
root.mainloop()