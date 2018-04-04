#github version
from Tkinter import *
from tkinter import filedialog
import os
import distutils.dir_util

settings = os.path.expanduser('~/bsettings.txt') 

def choosedirectory():
	root.directory = filedialog.askdirectory()
	with open(settings, "a") as f:
		f.write(root.directory + "\n")

def backupdirectory():
	root.backup = filedialog.askdirectory()
	with open(settings, "a") as f:
		f.write(root.backup + "\n")

def daychoosen(value):
	day = value
	with open(settings, "a") as f:
		f.write(day + "\n")

def copy_files():
	with open(settings, "r") as f:
		lines = list(line for line in f)

	file_path = lines[0]
	dest = lines[1]
	file_path = file_path.rstrip()
	dest = dest.rstrip()

	for subdir, dirs, files in os.walk(file_path):
		subdirs = os.path.join(subdir, subdir)
		dirpath = os.path.join(dirs, subdirs)
		distutils.dir_util.copy_tree(dirpath, dest)

	root.destroy()


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("320x140+%d+%d" % (x, y))

root = Tk()
root.title("Backup Utility")
center(root)
dirbutton = Button(root, text="Directory to backup:", command=choosedirectory)
ndirbutton = Button(root, text="Where to place backup:", command=backupdirectory)
submit = Button(root, text="Backup", command=copy_files)

dirbutton.place(relx=0.5, rely=0.15, anchor=CENTER)
ndirbutton.place(relx=0.5, rely=0.35, anchor=CENTER)
submit.place(relx=0.5, rely=0.9, anchor=CENTER)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
root.mainloop()