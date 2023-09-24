from xunit_example.WasRun import WasRun
from xunit_example.TestCase import TestCase

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun
    
    def testSetUp(self):
        self.test.run()
        assert self.test.wasSetUp