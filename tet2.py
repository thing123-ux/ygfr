class Student:
    class_name = "12A1"  # Static info for the class

    def __init__(self, name, math, literature, english):
        self.name = name
        self.math = float(math)
        self.literature = float(literature)
        self.english = float(english)

    def average_score(self):
        return (self.math + self.literature + self.english) / 3

    def display_info(self):
        print(f"Tên: {self.name}")
        print(f"Điểm Toán: {self.math}")
        print(f"Điểm Văn: {self.literature}")
        print(f"Điểm Anh: {self.english}")
        print(f"Điểm trung bình: {self.average_score():.2f}")

    @classmethod
    def from_string(cls, data_str):
        parts = data_str.split(", ")
        return cls(parts[0], parts[1], parts[2], parts[3])


    @staticmethod
    def get_class_name():
        return Student.class_name


# --- Demo ---
students = []

# Input students from user
n = int(input("Nhập số lượng học sinh: "))
for i in range(n):
    data = input(f"Nhập thông tin học sinh {i+1} (Tên, Điểm Toán, Điểm Văn, Điểm Anh): ")
    student = Student.from_string(data)
    students.append(student)

# Display all students
print("\n--- Danh sách học sinh ---")
for s in students:
    s.display_info()
    print("-" * 30)

# Sort students by average score
students.sort(key=lambda x: x.average_score(), reverse=True)

print("\n--- Danh sách học sinh theo điểm trung bình giảm dần ---")
for s in students:
    print(f"{s.name}: {s.average_score():.2f}")

# Print class info
print(f"\nTên lớp: {Student.get_class_name()}")