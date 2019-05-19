function tests = unitTests
    tests = functiontests(localfunctions);
end

% COLORS:

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

% FORWARD
function testForward(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()
    
    speed = 30
    
    forward(motor_left, motor_right, speed)
    
    testCase.verifyEqual(motor_left.Speed, speed)
    testCase.verifyEqual(motor_right.Speed, speed)
end

% Obstacle in Range
function testObstacleInRange_True(testCase)  
    actual = obstacleInRange(.154, 3)
    testCase.verifyEqual(actual, true)
end

function testObstacleInRange_False_Stage(testCase)  
    actual = obstacleInRange(.154, 1)
    testCase.verifyEqual(actual, false)
end

function testObstacleInRange_False_Distance(testCase)  
    actual = obstacleInRange(.254, 3)
    testCase.verifyEqual(actual, false)
end

% STOP
% stop function (speed should both be zero)
function testStop(testCase)  
    motor_left = dummyMotor()
    motor_right = dummyMotor()    
    
    stop_motors(motor_left, motor_right)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
end

% LEFT
function testLeft(testCase)  
    motor_left = dummyMotor()
    motor_right = dummyMotor()
    
    speed = 3
    time = 1
    
    left(motor_left, motor_right, speed, time)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
end

% RIGHT
function testRight(testCase)  
    motor_left = dummyMotor()
    motor_right = dummyMotor()
    
    speed = 3
    time = 1
    
    left(motor_left, motor_right, speed, time)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
end




    