

# MSG_ACCEPTED = "Congratulations, you are accepted!"
# MSG_REJECTED = "We regret to inform you that we will not be able to offer you admission."
MSG_SUCCESSFUL_APPLICANTS = "Successful applicants:"
# THRESHOLD = 60.0

N = int(input())
M = int(input())
students = [input().split() for _ in range(N)]
students = sorted(students, key=lambda x: (-float(x[2]), x[0], x[1]))
print(MSG_SUCCESSFUL_APPLICANTS)
for student in students[:M]:
    print(student[0], student[1])
