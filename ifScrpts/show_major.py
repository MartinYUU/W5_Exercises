#  Create a script named show_major.py that defines two variables for a student: 
# student_name and student_major. The student_major variable will contain a 
# code for the student’s major (e.g. ENG).

major_dict = {'BIOL' : ['Biology', 'Science Bldg, Room 310'],
              'CSCI' : ['Computer Science', 'Sheppard Hall, Room 314'],
              'ENG'  : ['English, Kerr Hall, Room 201'],
              'HIST' : ['History', 'Kerr Hall, Room 114'],
              'MKT'  : ['Marketing', 'Westly Hall, Room 314'],
              'unknown' : ['Unknown, ']
              }
student_name = input('What is your name?: ')
major_code = input('Enter the code for your major: ').upper()
print("student Name is: ", student_name)
match major_code :
    case 'BIOL' :
        print('Your major is:', major_dict['BIOL'])
    case 'CSCI' :
        print('Your major is:', major_dict['CSCI'])
    case 'ENG'  :
        print('Your major is:', major_dict['ENG'])
    case 'HIST' :
        print('Your major is:', major_dict['HIST'])
    case 'MKT'  :
        print('Your major is:', major_dict['MKT'])
    case other:
        print('Your major is:', major_dict['unknown'])