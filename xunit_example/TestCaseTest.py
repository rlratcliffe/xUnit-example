from xunit_example.WasRun import WasRun
from xunit_example.TestCase import TestCase

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun