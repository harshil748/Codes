from attendance.attendance_manager import AttendanceManager

def main():
    attendance_manager = AttendanceManager()
    n = int(input())
    for _ in range(n):
        record = input().strip()
        parts = record.split()

        if len(parts) < 3:
            continue

        employee_id = parts[0]
        status = parts[-1]
        name = " ".join(parts[1:-1])

        if attendance_manager.mark_attendance(employee_id, name, status):
            print("Attendance Marked")

    command = input().strip()
    if command == "VIEW":
        records = attendance_manager.view_attendance()
        print("Attendance Records:")
        for record in records:
            print(record)


if __name__ == "__main__":
    main()