
APPLICANTS_FILENAME = "applicant_list_5.txt"
# APPLICANTS_FILENAME = "applicants.txt"
departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]

dep_grade = {
    "Physics": 2,
    "Chemistry": 3,
    "Biotech": 3,
    "Mathematics": 4,
    "Engineering": 5,
}

departments_students = dict.fromkeys(departments, None)

N = int(input())
students_original = []
with open(APPLICANTS_FILENAME, 'r') as applicants_file:
    for line in applicants_file:
        students_original.append(line.split())

students_sorted = sorted(students_original, key=lambda x: (-float(x[2]), -float(x[3]), -float(x[4]), float(x[5]), x[0], x[1]))
for i in range(3):
    for dept in departments:
        if not departments_students[dept]:
            departments_students[dept] = []

        if len(departments_students[dept]) >= N:
            continue
        students_sorted = sorted(students_sorted, key=lambda x: (-float(x[dep_grade[dept]]), x[0], x[1]))
        m = N
        d_list = [x for x in students_sorted if x[6 + i] == dept]
        if len(d_list) > N - len(departments_students[dept]):
            m = m - len(departments_students[dept])
        d_list = d_list[:m]
        departments_students[dept].extend(d_list)
        students_sorted = [x for x in students_sorted if x not in d_list]


for dept, students in departments_students.items():
    print(f'\n{dept}')
    for student in sorted(students, key=lambda x: (-float(x[dep_grade[dept]]), x[0], x[1])):
        print(student[0], student[1], float(student[dep_grade[dept]]))
