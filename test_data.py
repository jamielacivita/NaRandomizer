# alway import unittest for tests
import unittest

#change below the the name of the module you are testing.
import data

# change below myfunc to match the name of the module you are testing.
class Test_myfunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is the setUpClass method.")
        print("It runs once to start the testing cycle.")

    @classmethod
    def tearDownClass(cls):
        print("This is the teardown method.")
        print("It runs once at the end of the testing cycle.")

    def setUp(self):
        print("This is the instance setup method.")
        print("It runs before each test is performed.  If you have three tests it will run three times.")

    def tearDown(self):
        print("This is the instance teardown method.")
        print("It runs after each test is performed.")

    # actual function / object tests start here.
    def test_hw(self):
        self.assertTrue(data.hw(),"Testing for truth of hw.")
