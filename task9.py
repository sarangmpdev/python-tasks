Student_list = {'Alice':85,'Evin':65,'Priya':88,'Arjun':79}

name=(input("'Enter the student's name: "))

if name in Student_list:
    mark=Student_list[name]
    print(f"{name}'s mark is: {mark}")

else:
    print('Student not found')