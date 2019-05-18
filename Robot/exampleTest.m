function tests = exampleTest
    tests = functiontests(localfunctions);
end

% LIBPOINTER is matlab equivalent to null object.

%% COLORS:

% BLACK:
function testIsBlack_True(testCase)
    actual = isBlack(libpointer, 24, libpointer)
    testCase.verifyEqual(actual, true)
end

function testIsBlack_False(testCase)
    actual = isBlack(libpointer, 26, libpointer)
    testCase.verifyEqual(actual, false)
end

function testIsBlack_Error(testCase)
    testCase.verifyError(@()isBlack(libpointer, "INVALID INPUT", libpointer), 'MATLAB:string:ComparisonNotDefined') 
end

% GREY/PURPLE
function testIsGreyOrPurple_GreyTruePurpleFalse(testCase)
    [isGrey, isPurple] = isGreyOrPurple(libpointer, 34, libpointer, 3)   
    testCase.verifyEqual(isGrey, true)
    testCase.verifyEqual(isPurple, false)
end

function testIsGreyOrPurple_GreyFalsePurpleTrue(testCase)
    [isGrey, isPurple] = isGreyOrPurple(libpointer, 34, libpointer, 4)   
    testCase.verifyEqual(isGrey, false)
    testCase.verifyEqual(isPurple, true)
end

% Incorrect reflected value + correct stage
function testIsGreyOrPurple_GreyFalsePurpleFalse_reflected(testCase)
    [isGrey, isPurple] = isGreyOrPurple(libpointer, 10, libpointer, 4)   
    testCase.verifyEqual(isGrey, false)
    testCase.verifyEqual(isPurple, false)
end

% Correct reflected value + incorrect stage
function testIsGreyOrPurple_GreyTruePurpleFalse_stage(testCase)
    [isGrey, isPurple] = isGreyOrPurple(libpointer, 34, libpointer, 3)   
    testCase.verifyEqual(isGrey, true)
    testCase.verifyEqual(isPurple, false)
end

function testIsGreyOrPurple_ErrorGrey(testCase)
    testCase.verifyError(@()isGreyOrPurple(libpointer, "INVALID INPUT", libpointer, "INVALID INPUT"), 'MATLAB:string:ComparisonNotDefined') 
end

% RED:
function testIsRed_True(testCase)
    actual = isRed(libpointer, 75, libpointer)
    testCase.verifyEqual(actual, true)
end

function testIsRed_False(testCase)    
    actual = isRed(libpointer, 10, libpointer)
    testCase.verifyEqual(actual, false) 
end

function testIsRed_Error(testCase)    
    testCase.verifyError(@()isRed(libpointer, "INVALID INPUT", libpointer), 'MATLAB:string:ComparisonNotDefined') 
end

% WHITE:
function testIsWhite_True(testCase)
    actual = isWhite(libpointer, 90, libpointer)
    testCase.verifyEqual(actual, true)
end

function testIsWhite_False(testCase)    
    actual = isWhite(libpointer, 10, libpointer)
    testCase.verifyEqual(actual, false) 
end

function testIsWhite_Error(testCase)    
    testCase.verifyError(@()isWhite(libpointer, "INVALID INPUT", libpointer), 'MATLAB:string:ComparisonNotDefined') 
end



