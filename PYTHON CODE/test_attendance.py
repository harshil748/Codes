import unittest
import os
from attendance.attendance_manager import AttendanceManager


class TestAttendanceManager(unittest.TestCase):
    def setUp(self):
        """Initialize a new AttendanceManager instance with a test file before each test"""
        self.test_file = "test_attendance.txt"
        # Ensure the test file doesn't exist before testing
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.attendance_manager = AttendanceManager(self.test_file)

    def tearDown(self):
        """Clean up the test file after each test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_mark_attendance(self):
        """Test marking attendance"""
        result = self.attendance_manager.mark_attendance("E001", "John Doe", "Present")
        self.assertTrue(result)

    def test_view_empty_attendance(self):
        """Test viewing attendance when no records exist"""
        records = self.attendance_manager.view_attendance()
        self.assertEqual(len(records), 0)

    def test_mark_and_view_attendance(self):
        """Test marking and then viewing attendance"""
        # Mark attendance for a few employees
        self.attendance_manager.mark_attendance("E001", "John Doe", "Present")
        self.attendance_manager.mark_attendance("E002", "Jane Smith", "Absent")
        self.attendance_manager.mark_attendance("E003", "Bob Johnson", "Late")

        # Check that all marked records are in the view
        records = self.attendance_manager.view_attendance()
        self.assertEqual(len(records), 3)
        self.assertIn("E001 John Doe Present", records)
        self.assertIn("E002 Jane Smith Absent", records)
        self.assertIn("E003 Bob Johnson Late", records)

    def test_multiple_attendance_records(self):
        """Test marking attendance multiple times"""
        # Mark attendance for the same employee with different statuses
        self.attendance_manager.mark_attendance("E001", "John Doe", "Present")
        self.attendance_manager.mark_attendance("E001", "John Doe", "Late")

        # Both records should be present (the system allows multiple entries)
        records = self.attendance_manager.view_attendance()
        self.assertEqual(len(records), 2)
        self.assertIn("E001 John Doe Present", records)
        self.assertIn("E001 John Doe Late", records)

    def test_file_persistence(self):
        """Test that attendance records persist in the file"""
        # Mark attendance
        self.attendance_manager.mark_attendance("E001", "John Doe", "Present")

        # Create a new instance pointing to the same file
        new_manager = AttendanceManager(self.test_file)

        # The new instance should be able to read the existing record
        records = new_manager.view_attendance()
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0], "E001 John Doe Present")


if __name__ == "__main__":
    unittest.main()
