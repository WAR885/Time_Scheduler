from tkinter import *
from ScheduleMenu import *

class PageController:
    def __init__(self, root: Tk):
        self.root = root
        self.screenContainer = Frame(root)
        self.screenContainer.pack(fill="both",expand=True)
        self.scheduleMenu = ScheduleInterface(self.screenContainer)
