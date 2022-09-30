def getdata():
    D = {}
    print(D)
    while True:
        student_id = input("Enter id: ")
        marks_list = input('Enters the marks sepparated by commas: ')
        moreStudents = input('Do you want to save results: ')
        if student_id in D:
            print('Study already enrolled')
        else:
            D[student_id] = marks_list.split(",")
        if moreStudents.lower() == 'no':
            return
