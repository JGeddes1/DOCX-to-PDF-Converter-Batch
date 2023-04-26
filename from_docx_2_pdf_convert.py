from docx2pdf import convert
from tkinter import filedialog
import os
from tkinter import *

# path = filedialog.askdirectory(master='', initialdir='', title="Select your Source directory", mustexist=True)


# convert("\\users\jgg513\\ADS-Easy\\arch-5293-1\\original\\12547\\2023-03-17\\M1D17_Clay_Pipes_Report.docx")

def Convert():

    path = filedialog.askdirectory(master='', initialdir='', title="Select your Source directory", mustexist=True)

# path = "W:\\users\\jgg513\\ADS-Easy\\arch-5235-1\\original\\12470\\2023-03-20\\documentation"

    files = os.listdir(path)

    convert(path, output_path=os.getcwd())



      
root = Tk()
main_container = Frame(root)
main_container.grid()
myButton = Button(main_container, text="Select Directory To Check for doc to pdf files",
                  command=Convert)

myButton.grid(column=0, row=0, padx=5 ,pady=5, sticky='w')
root.mainloop()  