from xunit_example.WasRun import WasRun

def main():
    test = WasRun("testMethod")
    print(test.wasRun)
    test.run()
    print(test.wasRun)