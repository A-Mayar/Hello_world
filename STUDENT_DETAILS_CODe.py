class student:
  def __init__(self,name,age,is_enrolled,gpa,gender):
    self.name = str(name)
    self.age= int(age)
    self.is_enrolled = bool(is_enrolled)
    self.gpa = float(gpa)
    self.gender = str(gender)
  
  def studentdetails(self):
    print("student details are as follows: "+self.name +str(self.age)+str(self.is_enrolled)+str(self.gpa)+self.gender)

STUDENT01 = student("KARIM",19,True,3.21,"MALE")

STUDENT01.studentdetails()
