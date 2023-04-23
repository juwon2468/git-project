def allocate_course_id(course_id_map, course_name):
    if course_name not in course_id_map:
        new_id = str(int(course_id_map['id']) + 1)
        course_id_map['id'] = new_id
        course_id_map[course_name] = new_id
        course_id_map[new_id] = course_name
        
        return course_id_map, new_id
    
    else:
        return course_id_map, course_id_map[course_name]
    
def get_gpa_score(gpa):
    match gpa:
        case 'A+':
            return 4.5
        case 'A':
            return 4
        case 'B+':
            return 3.5
        case 'B':
            return 3
        case 'C+':
            return 2.5
        case 'C':
            return 2
        case 'D+':
            return 1.5
        case 'D':
            return 1
        case 'F':
            return 0
        

def input_process(course_id_map):
    course_name = input('과목명을 입력하세요: ')
    course_id_map, course_id = allocate_course_id(course_id_map, course_name)
    
    credit = input('학점을 입력하세요: ')
    
    gpa = input('평점을 입력하세요: ')
        
    return (course_id, int(credit), gpa)


def calculation_process(submit_credit, archive_credit, submit_gpa, archive_gpa):
    print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str(submit_gpa) + ')')
    print('열람용: ' + str(archive_credit) + '학점' + '(GPA: ' + str(archive_gpa) + ')')
    

course_id_map = {'id': 10000}
taken_course_list = []
submit_grade = {}
archive_grade = {}

while True:
    
    print('작업을 선택하세요')
    print('    1. 입력')
    print('    2. 출력')
    print('    3. 계산')

  
    user_input = input()
    

    if user_input == '1':
        user_course_id, user_credit, user_gpa = input_process(course_id_map)
        user_gpa_score = get_gpa_score(user_gpa)
        
        if user_course_id in archive_grade:
            if user_gpa_score > archive_grade[user_course_id][1]:
                archive_grade[user_course_id] = (user_credit, user_gpa_score)
        else:
            archive_grade[user_course_id] = (user_credit, user_gpa_score)
            
        if user_gpa_score > 0.0:
            if user_course_id in submit_grade:
                if user_gpa_score > submit_grade[user_course_id][1]:
                    submit_grade[user_course_id] = (user_credit, user_gpa_score)
            else:
                submit_grade[user_course_id] = (user_credit, user_gpa_score)

        taken_course_list.append((user_course_id, user_credit, user_gpa))
                
        print('입력되었습니다.')
        
    elif user_input == '2':
        for taken_course in taken_course_list:
            print('[' + course_id_map[taken_course[0]] + '] ', end='')
            print(str(taken_course[1]) + '학점: ' + taken_course[2])
        
    elif user_input == '3':
        submit_gpa, archive_gpa = 0.0, 0.0
        submit_credit, archive_credit = 0, 0
        for course_id in submit_grade:
            submit_gpa += submit_grade[course_id][0] * submit_grade[course_id][1]
            submit_credit += submit_grade[course_id][0]
        for course_id in archive_grade:
            archive_gpa += archive_grade[course_id][0] * archive_grade[course_id][1]
            archive_credit += archive_grade[course_id][0]
        submit_gpa /= submit_credit
        archive_gpa /= archive_credit
        calculation_process(submit_credit, archive_credit, submit_gpa, archive_gpa)
        break
        
    else:
        continue
        
print('프로그램을 종료합니다.')
