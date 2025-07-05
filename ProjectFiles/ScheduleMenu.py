from tkinter import *
from datetime import *
from tkinter import ttk

class ScheduleInterface:
    WEEKDAYS = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

    def __init__(self,screen: Frame):
        self.screen = screen
        self.containerCanvas = Canvas(screen,width=800,height=300)
        self.containerCanvas.place(relx=0.55,rely=0.3,anchor="n")
        self.scrollBar = ttk.Scrollbar(self.screen, orient=VERTICAL, command=self.containerCanvas.yview)
        self.scrollBar.pack(side=LEFT,fill=Y)
        self.containerCanvas.configure(yscrollcommand=self.scrollBar.set)
        self.containerCanvas.bind("<Configure>", lambda e: self.containerCanvas.configure(scrollregion=self.containerCanvas.bbox("all")))
        self.scheduleGrid = Frame(self.containerCanvas,borderwidth=5,relief="groove")
        self.scheduleGrid.pack(fill="both",expand=True)
        self.containerCanvas.create_window((0,0),window=self.scheduleGrid,anchor="nw")
        
        self.currDate = date.today()

        
        for i in range(7):
            label = Label(self.scheduleGrid,text=self.WEEKDAYS[i],padx=5,font=("Courier",15))
            label.grid(row=0,column=i+1)
        
        for j in range(24):
            currHour = j % 12
            if(j % 12 == 0):
                currHour = 12
            displayTime = ""
            if(currHour // 12 == 1 and j != 0):
                displayTime = str((currHour)) + "PM"
            else:
                displayTime = str(currHour) + "AM"
            label = Label(self.scheduleGrid,text=(displayTime),font=("Courier",10))
            label.grid(row=j+1,column=0)