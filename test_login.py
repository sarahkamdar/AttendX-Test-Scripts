
import unittest


def login(username, password):
    if username == "student" and password == "pass123":
        return True
    return False


class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertTrue(login("student", "pass123"))

    def test_invalid_login(self):
        self.assertFalse(login("student", "wrong"))


if __name__ == "__main__":
    unittest.main()
