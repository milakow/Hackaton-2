def count_potential_grade(student_grade):
    return student_grade + 1


def get_student_data():
    try:
        with open('students.csv') as f:
            file_lines = f.readlines()
            student_dict = {}
            for line in file_lines:
                stripped_line = line.rstrip('\n')
                list_data = stripped_line.split(';')
                if len(line) == 0:
                    break
                student_class = list_data[0]
                student_name = list_data[1]
                student_surname = list_data[2]
                student_grade = list_data[4]
                if student_grade == '-':
                    list_data.pop(4)
                    list_data.insert(4, '0')
                dict_keys = student_class + '_' + student_name + '_' + student_surname
                student_dict.update({dict_keys: list_data[1:5]})
            return student_dict
    except FileNotFoundError as e:
        print('This file does not exist.')


def prep_message(name, task, grade, pot_grade, date):
    with open('message.txt') as fmes:
        text = fmes.read()

    message = text.replace('[name]', name).replace('[missing tasks]', task).replace('[current grade]', str(grade)).replace('[potential grade]', str(pot_grade)).replace('[date]', date)
    return message


def main():
    date = 'next Monday- 4th of July'

    student_dict = get_student_data()
    for my_keys in student_dict:
        name = student_dict.get(my_keys)[0].title()
        task = student_dict.get(my_keys)[2]
        grade = int(student_dict.get(my_keys)[3])

        pot_grade = count_potential_grade(grade)
        student_dict = get_student_data()
        message = prep_message(name, task, grade, pot_grade, date)
        print(message, '\n')


if __name__ == '__main__':
    main()
