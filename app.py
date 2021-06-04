# Useful Modules
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import backend as bk

# Creating Master

root = Tk()


class GUI:
    def __init__(self, master):
        master.title("Dotted Puzzle Generator")

        # Defining size for the window
        self.size = (1430, 515)  # do not change this values as they are static

        # master.minsize(width=self.size[0], height=self.size[1])

        # some constant static variables
        self.top_labels_height = 40     # Top Label Height
        self.button_height = 2      # button height
        self.image_frames_height = 400  # image frame height

        self.top_labels = LabelFrame(master,  width=self.size[0], height=self.top_labels_height, bg='white').grid(
            row=0, column=0, columnspan=4)

        Label(self.top_labels, text="Original Image",
              fg='black', bg='white', font=("Helvetica")).grid(row=0, column=0)
        Label(self.top_labels, text="Black and White Image",
              fg='black', bg='white', font=("Helvetica")).grid(row=0, column=1)
        Label(self.top_labels, text="Puzzled Image",
              fg='black', bg='white', font=("Helvetica")).grid(row=0, column=2, columnspan=2)

        self.image_frames = [
            LabelFrame(master, width=self.size[0]//3,
                       height=self.image_frames_height).grid(row=1, column=0),
            LabelFrame(master, width=self.size[0]//3,
                       height=self.image_frames_height).grid(row=1, column=1),
            LabelFrame(
                master, width=self.size[0]//3, height=self.image_frames_height).grid(row=1, column=2, columnspan=2)
        ]

        self.images = [
            Label(self.image_frames[0], width=self.size[0]//3),
            Label(self.image_frames[1], width=self.size[0]//3),
            Label(self.image_frames[2], width=self.size[0]//3)
        ]

        Button(master, text="Load Image", width=43,
               height=self.button_height, bg='#FF9671', font=("Helvetica"), command=self.open).grid(row=2, column=0),
        Button(master, text="Black and White", width=43,
               height=self.button_height, bg='#FFC1B3', font=("Helvetica"), command=self.black_and_white).grid(row=2, column=1)
        Button(master, text="Generate Image", width=21,
               height=self.button_height, bg='#FFC75F', font=("Helvetica"), command=self.dotted_image).grid(row=2, column=2)
        Button(master, text="Show Image", width=21,
               height=self.button_height, bg='#FFC75F', font=("Helvetica")).grid(row=2, column=3)

    def open(self):
        self.file_path = filedialog.askopenfilename(
            initialdir='./Images', title="Select an image", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))

        img = Image.open(self.file_path).resize(
            (self.size[0]//3, self.image_frames_height), Image.ANTIALIAS)
        # img.save("./Temp/size.png")
        self.img = ImageTk.PhotoImage(img)
        self.images[0].config(image=self.img)
        self.images[0].grid(row=1, column=0)

    def black_and_white(self):
        img = Image.fromarray(bk.Image_converter().load_img(self.file_path))
        self.blc_img = ImageTk.PhotoImage(img.resize((self.size[0]//3,
                                                      self.image_frames_height), Image.ANTIALIAS))
        self.images[1].config(image=self.blc_img)
        self.images[1].grid(row=1, column=1)

    def dotted_image(self):
        img = Image.fromarray(bk.Image_converter().generate(self.file_path))
        self.dot_img = ImageTk.PhotoImage(img.resize((self.size[0]//3,
                                                      self.image_frames_height), Image.ANTIALIAS))
        self.images[2].config(image=self.dot_img)
        self.images[2].grid(row=1, column=2, columnspan=2)


e = GUI(root)


root.mainloop()
