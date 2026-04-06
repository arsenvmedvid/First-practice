def analyze_students(students):
    def validate_data():
        if not students:
            raise ValueError("Словник порожній!")
        for name, grades in students.items():
            if not isinstance(grades, list) or not grades:
                raise ValueError(f"Помилка у студента {name}")
            for g in grades:
                if not (0 <= g <= 100):
                    raise ValueError(f"Оцінка {g} поза межами 0-100")

    def calculate_student_average():
        return {name: round(sum(grades)/len(grades), 1) for name, grades in students.items()}

    def get_passed_students(averages):
        return {name: "Pass" if avg >= 60 else "Failed" for name, avg in averages.items()}

    def sort_student_by_marks(averages):
        return dict(sorted(averages.items(), key=lambda x: x[1], reverse=True))

    def get_failed_students(averages):
        return {name: avg for name, avg in averages.items() if avg < 60}

    def get_top_students(averages):
        return sorted(averages.items(), key=lambda x: x[1], reverse=True)[:3]

    validate_data()
    averages = calculate_student_average()
    
    result = {
        "students average": averages,
        "passed students": get_passed_students(averages),
        "top students list": sort_student_by_marks(averages),
        "failed_students": get_failed_students(averages),
        "top_students": get_top_students(averages)
    }
    return result

students_list = {
    "Ivan": [78, 82, 90],
    "Olena": [45, 60, 55],
    "Petro": [100, 95, 98],
    "Anna": [50, 40, 30],
    "Maria": [70, 75, 80]
}

stats = analyze_students(students_list)
for key, value in stats.items():
    print(f"{key}: {value}")