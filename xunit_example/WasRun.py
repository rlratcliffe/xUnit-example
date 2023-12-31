from xunit_example.TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "
    
    def testBrokenMethod(self):
        raise Exception

    def tearDown(self):
        self.log = self.log + "tearDown "