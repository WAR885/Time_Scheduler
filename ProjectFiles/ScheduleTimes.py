import datetime as dt

class ScheduleTimes:

    def __init__(self):
        self.currDate = dt.date.today
        self.currDayOfWeek = dt.date.weekday
        self.currTime = dt.time.hour