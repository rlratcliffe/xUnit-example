from xunit_example.TestCaseTest import TestCaseTest

def main():
    print(TestCaseTest("testTemplateMethod").run().summary())
    print(TestCaseTest("testResult").run().summary())
    print(TestCaseTest("testFailedResultFormatting").run().summary())
    print(TestCaseTest("testFailedResult").run().summary())
