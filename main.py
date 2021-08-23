from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
import memes_classifier

gui = Tk()
gui.geometry("320x60")
gui.title("PicMan-Mark-1")


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


def doStuff():
    folder = folderPath.get()
    if folder == '':
        messagebox.showerror("Error", "Folder Not Found.")
        return -1
    total_count, memeCount = memes_classifier.MemeClassifier(folder)
    if (total_count > -1):
        strr = "Successfully Processed!\n" + "Memes found : " + str(memeCount)
        messagebox.showinfo("Information", strr)
    else:
        messagebox.showerror("Error", "Something went wrong.")


folderPath = StringVar()
a = Label(gui, text="PicMan")
a.grid(row=0, column=1)

a = Label(gui, text="Path: ")
a.grid(row=1, column=0)

E = Entry(gui, textvariable=folderPath)
E.grid(row=1, column=1)
btnFind = ttk.Button(gui, text="Browse Folder", command=getFolderPath)
btnFind.grid(row=1, column=2)

c = ttk.Button(gui, text="Go", command=doStuff)
c.grid(row=1, column=3)
gui.mainloop()
