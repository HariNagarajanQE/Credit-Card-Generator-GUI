import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is the function called when the button is clicked
def btnClickFunction():
      print("Download my credit card generator from here: https://mega.nz/file/G3xSDAaR#BJQAdBtCggYrMPR_sE9o_WvR4svjcmIbyuXWwHd-u5A")
      makeProgress()
      makeProgress()
      makeProgress()
      makeProgress()
      makeProgress()
      makeProgress()
      makeProgress()
      makeProgress()
      makeProgress()
      makeProgress()


# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
	Progress_Bar['value']=Progress_Bar['value'] + 10
	root.update_idletasks()



root = Tk()

# This is the section of code which creates the main window
root.geometry('636x454')
root.configure(background='#0000FF')
root.title('Credit Card Gen')


# This is the section of code which creates a button
Button(root, text='Generate!', bg='#FF7F00', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=250, y=183)


# This is the section of code which creates the a label
Label(root, text='Click generate to generate your credit card :)', bg='#0000FF', font=('courier', 12, 'normal')).place(x=82, y=146)


# This is the section of code which creates a color style to be used with the progress bar
Progress_Bar_style = ttk.Style()
Progress_Bar_style.theme_use('clam')
Progress_Bar_style.configure('Progress_Bar.Horizontal.TProgressbar', foreground='#BCEE68', background='#BCEE68')


# This is the section of code which creates a progress bar
Progress_Bar=ttk.Progressbar(root, style='Progress_Bar.Horizontal.TProgressbar', orient='horizontal', length=255, mode='determinate', maximum=100, value=1)
Progress_Bar.place(x=172, y=224)


root.mainloop()