import unittest
import xmlrunner
import subprocess


class HelloWorldTest(unittest.TestCase):
    testScore = 0

    MAX_TESTED_SCORE = 20
    MAX_OVERALL_SCORE = 25

    def tearDown(self) -> None:
        if self.testScore == self.MAX_TESTED_SCORE:
            print("\nYour unit test score is ",
                  self.testScore,
                  " out of ",
                  self.MAX_TESTED_SCORE,
                  "\n")
        else:
            print("\nYour unit test score is ",
                  self.testScore,
                  " out of ",
                  self.MAX_TESTED_SCORE,
                  " (",
                  (self.testScore - self.MAX_TESTED_SCORE),
                  ")\n")

        print("The assignment is worth a total of ",
              self.MAX_OVERALL_SCORE,
              " where the remaining points")
        print("comes from grading related to documentation, algorithms, and other")
        print("criteria.\n\n")

    def test(self):
        # call hello world script command ##
        p = subprocess.Popen("python3 src/hello_world.py", stdout=subprocess.PIPE, shell=True)

        (output, err) = p.communicate()
        p_status = p.wait()

        self.assertEqual(b'Hello, World!\n', output)
        self.testScore += 10
        self.assertEqual(0, p_status)
        self.testScore += 10


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
