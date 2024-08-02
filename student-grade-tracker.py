class StudentGradeTracker:
    def __init__(self):
        # Initialize an empty dictionary to store student grades
        self.grades = {}

    def add_grade(self, student_name, subject, grade):
        # Add or update the grade for a student in a particular subject
        if student_name not in self.grades:
            self.grades[student_name] = {}
        self.grades[student_name][subject] = grade

    def view_grades(self, student_name):
        # View all grades for a specific student
        if student_name in self.grades:
            return self.grades[student_name]
        else:
            return f"No grades available for {student_name}"

    def calculate_average(self, student_name):
        # Calculate the average grade for a specific student
        if student_name in self.grades:
            subjects = self.grades[student_name]
            if subjects:
                average = sum(subjects.values()) / len(subjects)
                return average
            else:
                return "No grades available to calculate average."
        else:
            return f"No grades available for {student_name}"

    def generate_report(self):
        # Generate a report of all students and their average grades
        report = {}
        for student, subjects in self.grades.items():
            if subjects:
                average = sum(subjects.values()) / len(subjects)
                report[student] = average
        return report

# Example usage
if __name__ == "__main__":
    tracker = StudentGradeTracker()
    tracker.add_grade("Alice", "Math", 95)
    tracker.add_grade("Alice", "Science", 89)
    tracker.add_grade("Bob", "Math", 76)
    tracker.add_grade("Bob", "Science", 82)

    print("Alice's Grades:", tracker.view_grades("Alice"))
    print("Alice's Average Grade:", tracker.calculate_average("Alice"))
    print("Student Report:", tracker.generate_report())
