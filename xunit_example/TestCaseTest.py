from xunit_example.WasRun import WasRun
from xunit_example.TestCase import TestCase

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod " == test.log