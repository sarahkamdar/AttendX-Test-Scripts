
import unittest


def mark_attendance(student_id, status):
    if student_id and status in ["Present", "Absent"]:
        return "Attendance marked successfully"
    return "Invalid attendance details"


class TestAttendanceMarking(unittest.TestCase):

    def test_mark_present(self):
        result = mark_attendance("ST101", "Present")
        self.assertEqual(result, "Attendance marked successfully")

    def test_invalid_student(self):
        result = mark_attendance("", "Present")
        self.assertEqual(result, "Invalid attendance details")


if __name__ == "__main__":
    unittest.main()
