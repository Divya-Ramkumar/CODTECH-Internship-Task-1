#Student Grade Tracker 

class Student:
    def __init__(self, name):
        self.name = name
        self.mark = {}

    def add_mark(self, subject, mark):
        self.mark[subject] = mark

    def calculate_average(self):
        total = sum(self.mark.values())
        return total / len(self.mark)

    def get_letter_mark(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

def main():
    students = []

    while True:
        print("1. Add student")
        print("2. Add mark")
        print("3. Calculate average")
        print("4. Display grades")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student = Student(name)
            students.append(student)
        elif choice == "2":
            for i, student in enumerate(students):
                print(f"{i+1}. {student.name}")
            student_index = int(input("Enter student number: ")) - 1
            subject = input("Enter subject: ")
            mark = float(input("Enter grade: "))
            students[student_index].add_mark(subject, mark)
        elif choice == "3":
            for i, student in enumerate(students):
                print(f"{i+1}. {student.name}")
            student_index = int(input("Enter student number: ")) - 1
            average = students[student_index].calculate_average()
            letter_mark = students[student_index].get_letter_mark(average)
            gpa = students[student_index].get_gpa(average)
            print(f"Average: {average:.2f}")
            print(f"Letter Grade: {letter_mark}")
            print(f"GPA: {gpa:.2f}")
        elif choice == "4":
            for i, student in enumerate(students):
                print(f"{i+1}. {student.name}")
                for subject, mark in student.mark.items():
                    print(f"  {subject}: {mark:.2f}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()