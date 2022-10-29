def getstudent():
    # Dict variable "D"
    D = {}
    print(D)
    while True:
        student_id = input("Enter id: ")
        marks_list = input('Enters the marks sepparated by commas: ')
        moreStudents = input('Do you want to save results: ')
        # Let's check if student is in list
        if student_id in D:
            print('Already')
        else:
            D[student_id] = marks_list.split(",")
        if moreStudents.lower == "no":
            return
