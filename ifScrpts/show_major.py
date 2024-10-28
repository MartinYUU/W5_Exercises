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

major_code = input('Enter the code for the major you are looking for: ').upper()

match major_code :
    case 'BIOL' :
        print(major_dict['BIOL'])
    case 'CSCI' :
        print(major_dict['CSCI'])
    case 'ENG'  :
        print(major_dict['ENG'])
    case 'HIST' :
        print(major_dict['HIST'])
    case 'MKT'  :
        print(major_dict['MKT'])
    case other:
        print(major_dict['unknown'])