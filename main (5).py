#3.2 implement a function called sort_students that tasks a list of students objects as input and sorts the list based on their CGPA (Comulative Grade Point Average) in descending order. Each student object has the following attributes: name(string),roll number(string), and cgpa(float).Test the function with different input tests of students.
class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

  def sort_students(student_list):
#Sort the list of students in descending order of CGPA
    sorted_students = sorted(student_list,key=lambda student:student.cgpa,reverse=True)
#Syntax_lambda arg:exp
        
    return sorted_students
#Example usage:
students= [
Student("Alice","S123",3.7),
Student("Bob","S124",3.9),
Student("Charlie","S125",3.5),
Student("David","S126",3.8),
] 
sorted_students = sort_students(students)
#print the sorted list of students in sorted_students:
print("Name:{}, Roll number:{},CGPA:{}".format(student.name,student.roll_number,student.cpga))

    
