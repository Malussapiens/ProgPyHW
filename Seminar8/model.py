# список студентов
# {*student_id:[last_name,name],[subj_list]}
students = dict()
students = {1: ['Иванов', 'Иван'], 2: ['Петров', 'Петр']}

stud_id_count = 0

# Список предметов: [name1, name2, ....]
# subjects = list()
subjects = ['Химия', 'Физика', 'Математика']

# Список оценок студентов по предметам
# {stud_id:{subj_id:[marks]}}
stud_marks = [(1, 'Химия', [5, 4, 3, 5]),
              (1, 'Математика', [5, 3, 3]),
              (2, 'Физика', [5]),
              (2, 'Химия', [3])]

# список оценок
marks = ['1', '2', '3', '4', '5']

# получить значение счетчика student_id
def get_stud_id_count():
    global stud_id_count
    return stud_id_count

# установка значения счетчика student_id
def set_stud_id_count(value:int):
    global stud_id_count
    stud_id_count = value

# инициализация счетчика student_id
def init_stud_id_count():
    keys = list(students.keys())
    if len(keys) > 0:
        set_stud_id_count(max(keys))

# увеличиваем значение счетчика student_id
def inc_stud_id_count():
    set_stud_id_count(get_stud_id_count() + 1)

# получение списка предметов
def get_subjects_list():
    return tuple(subjects)

# добавление записи о предмете в список предметов
def add_subject(subj_name:str):
    if subj_name not in subjects:
        subjects.append(subj_name)

# возвращает кортеж с данными о студенте (id, имя, фамилия) по id
def get_student_entry(key):
    return tuple([key, *dict.get(students, key)])

# возвращает кортеж кортежей с данными о студентах
def get_students_keys():
    return tuple(students.keys())
    
# добавляет запись о студенте в список студентов
def add_student(full_name:tuple): 
    inc_stud_id_count()
    students[get_stud_id_count()] = list(full_name)

# возвращает список оценок студента по предмету
def get_student_marks(student_id:int):
    return tuple(filter(lambda x: x[0] == student_id, stud_marks))

# проверяет, есть ли предмет в списке оценок студента
def is_subj_in_list(student_id:int, subj:str):
    return len(list(filter(lambda x: x[1] == subj, get_student_marks(student_id)))) > 0

# добавляет предмет в список оценок студента
def set_subj_to_student(stud_id:int, subj:str):
    if not is_subj_in_list(stud_id, subj):
        set_student_mark(stud_id, subj, 0)

# Добавляет предметы из списка предметов в список оценок студента
def init_student_marks(stud_id:int):
    for subj in subjects:
        set_subj_to_student(stud_id, subj)

# добавляет оценку в список оценок студента по предмету
def set_student_mark(student_id:int, subj:str, mark:int=0):
    if mark > 0:
        mark = [mark]
    else:
        mark = []
    entry = [student_id, subj, mark]
    # todo: переписать данный блок кода с учетом функции is_subj_in_list()
    index = list(filter(lambda x: x[1][0] == student_id and x[1][1] == subj, enumerate(stud_marks)))
    if len(index)>0:
        if len(mark) > 0:
            stud_marks[index[0][0]][2].append(*mark)
    else:
        stud_marks.append(tuple(entry))

