"""
pass
"""
# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import FirstLoad
import LoadLang
import StartGame


class GameMain(FirstLoad.FirstLoad,LoadLang.LoadLang,StartGame.StartGame):
    """
    pass
    """

    def main(self):
        """
        pass
        """
        self.load_gui()
        self.load_save()
        self.win.mainloop()


if __name__ == '__main__':
    GameMain_v = GameMain()
    GameMain_v.main()
