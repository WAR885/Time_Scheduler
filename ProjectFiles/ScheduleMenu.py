from tkinter import *
from datetime import *
from tkinter import ttk
from ScheduleTimes import *

class ScheduleInterface:
    WEEKDAYS = ('Mon','Tues','Wed','Thur','Fri','Sat','Sun')
    timePanels = list()

    def __init__(self,screen: Frame):

        width = 750
        height = 300

        self.screen = screen

        #Top frame for options panel
        self.optionsFrame = Frame(self.screen,width=width,height=height)
        self.optionsFrame.pack(side="top",fill="x",expand=True)

        #Bottom frame for schedule grid
        self.scheduleFrame = Frame(self.screen,borderwidth=5,relief="groove",width=width,height=height)

        #creating internal canvas(Needed for scrollable pane)
        self.containerCanvas = Canvas(self.scheduleFrame,width=width,height=500)
        self.containerCanvas.pack(fill="both",expand=True)
        self.scrollBar = ttk.Scrollbar(self.scheduleFrame, orient=VERTICAL, command=self.containerCanvas.yview)
        self.containerCanvas.configure(yscrollcommand=self.scrollBar.set)

        #creating frame for the grid
        self.scheduleGrid = Frame(self.containerCanvas)
        self.scheduleGrid.bind("<Configure>", lambda e: self.containerCanvas.configure(scrollregion=self.containerCanvas.bbox("all")))
        self.containerCanvas.bind("<Configure>",self.__resizeCanvasWidth)
        self.windowId = self.containerCanvas.create_window((0,0),window=self.scheduleGrid,anchor="nw")
        self.containerCanvas.grid(row=0,column=1,sticky="nsew")

        #setting scrollbar in grid
        self.scrollBar.grid(row=0,column=0,sticky="ns")


        self.scheduleFrame.pack(side="bottom",fill="x",expand=True)

        self.scheduleFrame.grid_columnconfigure(1,weight=1)
        self.scheduleFrame.grid_rowconfigure(0,weight=1)

        self.weekSchedule = ScheduleTimes()

        
        for i in range(7):
            label = Label(self.scheduleGrid,text=f"{self.WEEKDAYS[i]}, {self.weekSchedule.weekDays[i].strftime("%m/%d")}",padx=5,font=("Courier",10),borderwidth=1,relief="solid")
            self.scheduleGrid.columnconfigure(i+1,weight=1)
            self.containerCanvas.columnconfigure(i+1,weight=1)
            label.grid(row=0,column=i+1,sticky="nsew")
        
        for j in range(24):
            currHour = j % 12
            if(j % 12 == 0):
                currHour = 12
            displayTime = ""
            if(j // 12 == 1):
                displayTime = str((currHour)) + "PM"
            else:
                displayTime = str(currHour) + "AM"
            label = Label(self.scheduleGrid,text=(displayTime),font=("Courier",10),borderwidth=1,relief="solid")
            label.grid(row=j+1,column=0, sticky="nsew")

        i = 0
        j = 0
        for i in range(7):
            for j in range(24):
                self.timePanels.append(Label(self.scheduleGrid,borderwidth=1,relief="solid"))
                self.timePanels[len(self.timePanels)-1].grid(row=j+1,column=i+1,sticky="nsew")
        self.__updatePanelHighlights()
        
    def __resizeCanvasWidth(self, event):
        self.containerCanvas.itemconfig(self.windowId,width = event.width)

    def __updatePanelHighlights(self):
        panels = self.timePanels
        currDay = self.weekSchedule.currDayOfWeek
        currTime = self.weekSchedule.currTime
        panels[(currDay)*24+currTime].configure(bg="gray")