# xunit-example
Part 2 of 'Test-Driven Devlopment by Example' by Kent Beck

# TODOs (copied from book)
- ~~Invoke test method~~
- ~~Invoke setUp first~~
- ~~Invoke tearDown afterward~~
- Invoke tearDown even if the test method fails
- ~~Run multiple tests~~
- ~~Report collected results~~
- ~~Log string in WasRun~~
- ~~Report failed tests~~
- Catch and report setUp errors
- Create TestSuite from a TestCase class

# Quotes

"Driving a testing tool using the testing tool itself to run the tests may seem a bit like performing brain surgery on yourself. ('Don't touch those motor centers - oh, too bad, game over') It will get weird from time to time."

"1. Arrange - Create some objects. 2. Act - Simulate them. 3. Assert - Check the results."

"Test coupling has an obvious nasty effect, in that breaking one test causes the next ten to fail even though the code is correct... Test coupling - don't go there."

"If we make a mistake implementing this, then we won't be able to see the mistake because the exceptions won't be reported."

"When I pick the next test to implement, I find a test that will teach me something and which I have confidence I can make work. If I get that test working but get stuck on the next one, then I consider backing up two steps."

"When I'm faced with a new programming language, I implement xUnit. By the time I have the first eight to ten tests running, I have explored many of the facilities I will be using in daily programming."