from teacher.models import Student

def get_student_by_faculty_no(faculty_no):
    return Student.objects.get(faculty_no=faculty_no)