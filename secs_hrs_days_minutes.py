class Time:
    def read(self,seconds):
        self.seconds=seconds
    def to_convert(self):
        self.minutes=self.seconds//60
        self.hours=self.seconds//3600
        self.days=self.days//86400
    def display(self):
       print("Hours:",self.hours)
       print("Minutes:",self.minutes)
       print("Days:",self.day)
    t=time()
    t.read(86400)
    t.to_convert()
    t.display()
