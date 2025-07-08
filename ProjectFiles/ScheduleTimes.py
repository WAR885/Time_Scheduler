from datetime import *

class ScheduleTimes:


    def __init__(self):
        self.currDate = date.today()
        self.currDayOfWeek = self.currDate.weekday()
        self.currTime = datetime.now().hour
        self.weekStart = (date.today() - timedelta(days=self.currDayOfWeek))
        self.weekDays = list()
        for i in range(7):
            self.weekDays.append((self.weekStart + timedelta(days=i)))
    
    @property
    def currDate(self):
        return self._currDate
    
    @currDate.setter
    def currDate(self, value):
        self._currDate = value

    @property
    def currDayOfWeek(self):
        return self._currDayOfWeek
    
    @currDayOfWeek.setter
    def currDayOfWeek(self, value):
        self._currDayOfWeek = value
    
    @property
    def currTime(self):
        return self._currTime
    
    @currTime.setter
    def currTime(self, value):
        self._currTime = value
    
    @property
    def weekStart(self):
        return self._weekStart
    
    @weekStart.setter
    def weekStart(self, value):
        self._weekStart = value
    
    @property
    def weekDays(self):
        return self._weekDays
    
    @weekDays.setter
    def weekDays(self, value):
        self._weekDays = value
    
    def updateDateOrTime(self):
        self.currDate = date.today
        self.currDayOfWeek = date.weekday
        self.currTime = datetime.now().hour
        self.weekStart = date.today - timedelta(self.currDayOfWeek)
        if self.currDate not in self.weekDays:
            self.weekDays.clear()
            for i in range(7):
                self.weekDays.add(self.weekStart + timedelta(i))