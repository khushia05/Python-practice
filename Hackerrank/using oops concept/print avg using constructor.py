class Student:
    def __init__(self,subject,marks):
        self.subject=subject
        self.marks=marks
    def avg(self):
        s=0
        for i in self.marks:
            s+=i
             
        print("average of marks",s/3)
obj=Student(["math","hindi","geo"],[100,100,100])        
obj.avg()        