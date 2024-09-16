import unittest
import subprocess

class EmployeeIdVerificationTest(unittest.TestCase):
    def run_process(self, first_name, last_name, id_code):
        command = ['python3', 'employeeIdCode.py', first_name, last_name, id_code]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def test_simple(self):
        expected = "PASS"
        self.assertEqual(self.run_process("Jigarius", "Caesar", "CAJI202002196"), expected)

if __name__ == "__main__":
    unittest.main()