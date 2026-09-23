import unittest
from application.app import get_release_status


class TestReleaseManagementApp(unittest.TestCase):

    def test_release_status(self):
        result = get_release_status()
        self.assertEqual(
            result,
            "This test shoud fail"
        )


if __name__ == "__main__":
    unittest.main()