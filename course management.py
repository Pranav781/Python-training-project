#project -- student course managemnt system list tuple dist set ,
# student name list() , course detail , unique skills sets() and student information

student_names = []
student_records = {}

def add_student():
    name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")
    course_name = input("Enter Course Name: ")
    course_info = {"title": course_name}
    
    skills_input = input("Enter skills: ")

    unique_skills = set()

    temp_list = skills_input.split(",")
    for s in temp_list:
        unique_skills.add(s)
    
    student_names.append(name)
    student_records[student_id] = {
        "name": name,
        "course": course_info,
        "skills": unique_skills
    }
    print(f"Record for {name} added!")

def display_students():
    if not student_records:
        print("No records found.")
        return     
    for sid, info in student_records.items():
        print(f"\nID: {sid} | Name: {info['name']}")
        print(f"Course: {info['course']['title']}")
        print(f"Unique Skills: {', '.join(info['skills'])}")

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        break