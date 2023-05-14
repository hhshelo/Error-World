"""
pass
"""
# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from tkinter import Tk, Canvas
from PIL import Image, ImageTk

load_gui = None
load_save = None
win = None


class FirstLoad:
    """
    pass
    """

    def __init__(self):
        super().__init__()
        self.role_r4 = None
        self.role_r3 = None
        self.role_r2 = None
        self.role_r1 = None
        self.role_l4 = None
        self.role_l3 = None
        self.role_l2 = None
        self.role_l1 = None
        self.role = None
        self.game_img = None
        self.image2 = None
        self.game_img = None
        self.image1 = None
        self.game = None
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
        self.win.bind("<1>", self._start_game)
        self.win.focus_set()

    def load_title(self):
        """
        pass
        """
        self.height = self.win.winfo_height()
        self.width = self.win.winfo_width()
        self.game = Canvas(self.win, height=self.height, width=self.width, bg="#000000")
        self.load_title_img()
        self.game_img = self.game.create_image(0, 0, image=self.image1, anchor='nw')
        self.game.pack()

    def load_title_img(self):
        """
        pass
        """
        temp_img = Image.open('img\\title.gif')
        temp_img = temp_img.resize((self.width, self.height))
        self.image1 = ImageTk.PhotoImage(temp_img)

    def _start_game(self, event):
        self.game.delete(self.game_img)
        self.display_role()

    def load_role_img(self):
        """
        pass
        """
        temp_img = Image.open('img\\role\\l1.png')
        self.role_l1 = ImageTk.PhotoImage(temp_img)

        temp_img = Image.open('img\\role\\l2.png')
        self.role_l2 = ImageTk.PhotoImage(temp_img)

        temp_img = Image.open('img\\role\\l3.png')
        self.role_l3 = ImageTk.PhotoImage(temp_img)

        temp_img = Image.open('img\\role\\l4.png')
        self.role_l4 = ImageTk.PhotoImage(temp_img)

        temp_img = Image.open('img\\role\\r1.png')
        self.role_r1 = ImageTk.PhotoImage(temp_img)

        temp_img = Image.open('img\\role\\r2.png')
        self.role_r2 = ImageTk.PhotoImage(temp_img)

        temp_img = Image.open('img\\role\\r3.png')
        self.role_r3 = ImageTk.PhotoImage(temp_img)

        temp_img = Image.open('img\\role\\r4.png')
        self.role_r4 = ImageTk.PhotoImage(temp_img)

    def display_role(self):
        """
        pass
        """
        self.role = self.game.create_image(self.width // 2, self.height // 2, image=self.role_l1, anchor='nw')

    def display_role(self):
        """
        pass
        """
        self.role = vFirstLoad.game.create_image(self.width // 2, self.height // 2, image=self.role_l1, anchor='nw')


vFirstLoad = FirstLoad()


class GameMain:
    """
    pass
    """

    def main(self):
        """
        pass
        """
        vFirstLoad.load_gui()
        vFirstLoad.load_save()
        vFirstLoad.win.mainloop()


if __name__ == '__main__':
    GameMain_v = GameMain()
    GameMain_v.main()
