
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk
from  PIL import Image

window = tk.Tk()
window.title('Instagram')
window.geometry('800x500')
window.configure(bg='gray')

from image import MyImage
import ImageProcessingProject
import ImageProcessingFunction

class Ime:
    def __init__(self):
        self.path=" "
    def set_path(self,p):
        self.path=p
    def get_path(self):
        return self.path

naziv_slike=Ime()

def upload():
    root = Tk()
    root.filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #image=Image.open(root.filename)
    img = ImageTk.PhotoImage(Image.open(root.filename))
    label2 = Label(image=img)
    label2.image = img
    label2.grid(column=2, row=8)
    slika_path=root.filename
    naziv_slike.set_path(root.filename)
    root.mainloop()



ttk.Label(window, text = "Instagram Filters", 
          background = 'black', foreground ="white", 
          font = ("Maiandra GD", 15)).grid(row = 1, column = 1)

buttonUpload = tk.Button(text="Upload an image",font = ("Maiandra GD", 13), width=13, height=2,
                         bg="thistle",fg="black",command=upload)
buttonUpload.grid(column = 0, row = 2)

ttk.Label(window, text = "Select the Filter:",font = ("Maiandra GD", 13)).grid(column = 0,
          row = 3, padx = 10, pady = 25)

n = tk.StringVar()
comboboxFilter = ttk.Combobox(window, height=15, width = 30, textvariable = n)
# Adding combobox drop down list
comboboxFilter['values'] = (' Adjust', 
                          ' Brightness',
                          ' Contrast',
                          ' Warmth',
                          ' Saturation',
                          ' Fade',
                          ' Highlights',
                          ' Shadows',
                          ' Vignette',
                          ' Tilt shift',
                          ' Blur',
                          ' Sharpen',
                          ' Zoom')
comboboxFilter.grid(column = 1, row = 3)
comboboxFilter.current()

ttk.Label(window, text = "Change Value:",
          font = ("Maiandra GD", 13)).grid(column = 0,
          row = 4, padx = 10, pady = 25)

slider =ttk.Spinbox(window, from_=0, to=100)
slider.grid(column = 1, row = 4)

#def preview_filter(slika):
    #current_filter = comboboxFilter.get()
    #current_value = slider.get()

    #func_map = {#' Adjust':,
                #  ' Brightness': ImageProcessingProject.brightness(slika,current_value),
                  #' Contrast':,
                 # ' Warmth':ImageProcessingFunction.warmmth(slika,current_value),
                  #' Saturation':,
                  #' Fade':,
                  #' Highlights',
                  #' Shadows',
                  #' Vignette',
                  #' Tilt shift',
                  #' Blur',
                #  ' Sharpen': ImageProcessingProject.sharpen(slika,current_value)
                  #' Zoom'
    #}
   # func = func_map.get(current_filter)

   # func()

#buttonPreview = tk.Button(text="Preview",font = ("Maiandra GD", 13), width=13, height=2,
                         # bg="thistle",fg="black")# command=preview_filter(slika))

#buttonPreview.grid(column = 0, row = 5)
def applyFilter():
    prom=naziv_slike.get_path()

    if comboboxFilter.get()=="Brightness":
        root = Tk()
        label3 = Label(root, text=prom)
        print(prom)
        root.mainloop()
        #ImageProcessingProject.brightness(prom,slider.get())
buttonSave = tk.Button(text="Save and show",font = ("Maiandra GD", 13), width=13, height=2,
                       bg="thistle",fg="black", command= applyFilter)
buttonSave.grid(column = 0, row = 6)
window.mainloop()



