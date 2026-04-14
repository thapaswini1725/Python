class convertor:
 def to_inches(self,inches):
     self.inches=inches
 def to_feet(self):
     self.feet=self.inches/12
 def display(self):
     print("inches:",self.inches)
     print("feet:",self.feet)
c=convertor()
c.to_inches(65)
c.to_feet()
c.display()
