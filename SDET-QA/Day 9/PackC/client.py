import sys
sys.path.append("/SDET-QA/Day 9/PackA")
sys.path.append("/SDET-QA/Day 9/PackB")

#Approcah 1
# import emp
#
# empobj=emp.Employee(100,"Raj",1500000)
# empobj.displayemp()
#
# import stu
#
# stuobj=stu.Student(100,"Raj",'B')
# stuobj.displaystu()

#Approach 2
from emp import Employee
empobj=Employee(100,"Raj",1500000)
empobj.displayemp()

from stu import Student
stuobj=Student(100,"Raj",'B')
stuobj.displaystu()