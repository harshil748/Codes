from .employee import Employee
import os

class AttendanceManager:
    def __init__(self, file_path="attendance.txt"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                pass

    def mark_attendance(self, employee_id, name, status):
        employee = Employee(employee_id, name, status)
        with open(self.file_path, "a") as f:
            f.write(f"{employee}\n")
        return True

    def view_attendance(self):
        records = []
        try:
            with open(self.file_path, "r") as f:
                records = f.read().splitlines()
                if records and records[0] == "":
                    records = []
        except FileNotFoundError:
            pass

        return records
