student = {
    "First name" : "Gorgos",
    "last name" : "Tammo",
    "favourite course" : "Programering 1"


}

#1
print()
print(f"Student full name : {student['First name']} {student['last name']}")


#2
print()
student["favourite course"] = "ITF10219 Programmering 1"
print(student)

#3
student['alder'] = 21
print(student)