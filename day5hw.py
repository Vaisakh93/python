
frontend_students = {"Anita", "Rohan", "Kishor"}
backend_students = {"Rohan", "Meena", "Farhan"}

backend_students.add("Sanjay")

frontend_students.remove("Kishor")

both_courses = frontend_students & backend_students

only_backend = backend_students - frontend_students

total_unique_students = len(frontend_students | backend_students)

course_dict = {"Frontend": len(frontend_students),"Backend": len(backend_students)}

for course, count in course_dict.items():print(f"Course: {course}, Students: {count}")

full_course_dict = {**course_dict,"Fullstack": course_dict["Frontend"] + course_dict["Backend"]}

print("\nFrontend Students:", frontend_students)
print("Backend Students:", backend_students)
print("Students in Both Courses:", both_courses)
print("Students Only in Backend:", only_backend)
print("Total Unique Students:", total_unique_students)
print("Course Dictionary:", course_dict)
print("Full Course Dictionary:", full_course_dict)
