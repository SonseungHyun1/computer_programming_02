students = ["홍길동","주동철","배정훈"]
def call_students(parameeters):
    last = ""
    for i in parameeters:
        print(i)
        last = i
    return last

call_students(students)
