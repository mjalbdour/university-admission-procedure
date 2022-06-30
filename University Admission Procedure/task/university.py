

MSG_ACCEPTED = "Congratulations, you are accepted!"
MSG_REJECTED = "We regret to inform you that we will not be able to offer you admission."
THRESHOLD = 60.0

exams = [float(input()) for _ in range(3)]
avg = sum(exams) / len(exams)
print(avg)
print(MSG_ACCEPTED) if avg >= THRESHOLD else print(MSG_REJECTED)
