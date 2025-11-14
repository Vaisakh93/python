
python_students = {"Amit", "Riya", "Karan"}
data_science_students = {"Riya", "Neha", "Vivek"}

python_students.add("Sonia")

data_science_students.remove("Neha")

both_courses = python_students & data_science_students

only_python = python_students - data_science_students

all_students = python_students | data_science_students

course_dict = {"Python": len(python_students),"Data Science": len(data_science_students)}

for course, count in course_dict.items():print(f"Course: {course}, Students: {count}")

growth_dict = {course: count * 2 for course, count in course_dict.items()}

print("\nPython Students:", python_students)
print("Data Science Students:", data_science_students)
print("Students in Both Courses:", both_courses)
print("Only Python Students:", only_python)
print("All Students:", all_students)
print("Original Course Dictionary:", course_dict)
print("Growth Dictionary (values doubled):", growth_dict)
