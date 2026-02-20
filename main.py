# AIM: Task List Manager
# Coder:
# Date:
print("List of Students:")

cet = {"Alice", "Bob", "Charlie", "Frank"}
jee = {"Bob", "Eve", "Frank", "Heidi"}
neet = {"Bob", "Charlie", "Karl", "Liam"}

print(f"CET Students: {cet}")
print(f"JEE Students: {jee}")
print(f"NEET Students: {neet}")

all_students = cet | jee | neet
print(f"All Students: {all_students}")

all_exams = cet & jee & neet
print(f"All Exams: {all_exams}")

jee_not_neet = jee - neet
print(f"JEE but not for NEET: {jee_not_neet}")

cet_and_neet_not_jee = (cet & neet) - jee
print(f"CET and NEET but not for JEE: {cet_and_neet_not_jee}")

# Write your code here
# TODO: Add & Print new Task from user

# TODO: Edit & Print task selected by User

# TODO: Remove & Print a Task selected by User

# TODO: Sort & Print the Tasks

