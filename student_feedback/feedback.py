def add_feedback():
    name = input("Enter student name: ")
    feedback = input("Enter feedback: ")
    f = open("feedback.txt", "a")
    f.write(name + ":" + feedback + "\n")
    f.close()
    print("Feedback added successfully!")

def display_all():
    f = open("feedback.txt", "r")
    content = f.read()
    print("\n--- All Student Feedback ---")
    print(content)
    f.close()

def search_feedback():
    name_to_find = input("Enter the student name to search: ")
    f = open("feedback.txt", "r")
    found = False
    for line in f:
        if name_to_find.lower() in line.lower():
            print("Record Found:", line.strip())
            found = True
    if not found:
        print("No feedback found for that name.")
    f.close()

add_feedback()
search_feedback()
display_all()

