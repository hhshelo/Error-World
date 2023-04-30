"""
pass
"""
from tkinter import *
from PIL import Image, ImageTk


class FirstLoad(object):
    """
    pass
    """

    def __init__(self):
        self.bg_img = None
        self.image2 = None
        self.bg_img = None
        self.image1 = None
        self.bg = None
        self.width = None
        self.height = None
        self.win = None

    def load_save(self):
        """
        pass
        """
        pass

    def load_gui(self):
        """
        pass
        """
        self.win = Tk()
        self.win.title('Error World')
        self.win.state('zoomed')
        self.win.update()
        self.load_title()
        self.win.bind("<1>")
        self.win.focus_set()

    def load_title(self):
        """
        pass
        """
        self.height = self.win.winfo_height()
        self.width = self.win.winfo_width()
        self.bg = Canvas(self.win, height=self.height, width=self.width, bg=self.image2)
        self.load_img()
        self.bg_img = self.bg.create_image(0, 0, image=self.image1, anchor='nw')
        self.bg.pack()

    def load_img(self):
        """
        pass
        """
        image = Image.open('img\\title.gif')
        image = image.resize((self.width, self.height))
        self.image1 = ImageTk.PhotoImage(image)


if __name__ == '__main__':
    FirstLoad_v = FirstLoad()
    FirstLoad_v.load_gui()
