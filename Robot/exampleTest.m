function tests = exampleTest
    tests = functiontests(localfunctions);
end

%% Test Functions
function testFunctionOne(testCase)
    actual = findzero(2,3.5,0)
    expected = -1.0945    
    testCase.verifyEqual(actual, expected)
end
