function tests = integrationTests
    tests = functiontests(localfunctions);
end




function test_tc1_1(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 90, 90, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'forward')
        
    doAction(action, motor_left, motor_right, libpointer, 2)
    
    testCase.verifyEqual(motor_left.Speed, 14)
    testCase.verifyEqual(motor_right.Speed, 14)
end

% 
function test_tc1_2(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 75, 75, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'fastForward')
        
    doAction(action, motor_left, motor_right, libpointer, 1)
    
    testCase.verifyEqual(motor_left.Speed, 30)
    testCase.verifyEqual(motor_right.Speed, 30)
end

% 
function test_tc1_3(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 40, 40, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'slowForward')
        
    doAction(action, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 10)
    testCase.verifyEqual(motor_right.Speed, 10)
end

function test_tc1_4(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 40, 40, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'slowForward')
        
    doAction(action, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 10)
    testCase.verifyEqual(motor_right.Speed, 10)
end

% 
function test_tc1_5(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 101, 101, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'stop')
        
    doAction(action, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
end




function test_tc2_1(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()
    
%     Non-white; white
    action = resolveAction(libpointer, libpointer, 101, 91, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'left')        
    doAction(action, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
    
%     Non-red; red
    action2 = resolveAction(libpointer, libpointer, 101, 72, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action2, 'left')        
    doAction(action2, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
    
%     Non-black; grey
    action3 = resolveAction(libpointer, libpointer, 101, 40, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action3, 'left')        
    doAction(action3, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)   
end

function test_tc2_2(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()
    
%     Non-white; white
    action = resolveAction(libpointer, libpointer, 91, 101, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'right')        
    doAction(action, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
    
%     Non-red; red
    action2 = resolveAction(libpointer, libpointer, 72, 101, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action2, 'right')        
    doAction(action2, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
    
%     grey; black
    action3 = resolveAction(libpointer, libpointer, 40, 20, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action3, 'right')        
    doAction(action3, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)   
end










% Stop when obstalce is within distance .20 and stage 3
function test_tc3_1(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 101, 101, libpointer, libpointer, libpointer, .2, 3)
    testCase.verifyEqual(action, 'stop')
        
    doAction(action, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
end

% Restart after stopping because of obstacle
% Car sensors see white
function test_tc3_2(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action1 = resolveAction(libpointer, libpointer, 91, 91, libpointer, libpointer, libpointer, .2, 3)
    testCase.verifyEqual(action1, 'stop')
        
    doAction(action1, motor_left, motor_right, libpointer, 3)
    
    testCase.verifyEqual(motor_left.Speed, 0)
    testCase.verifyEqual(motor_right.Speed, 0)
    
%     Remove obstacle, i.e. change distance
    
    action2 = resolveAction(libpointer, libpointer, 91, 91, libpointer, libpointer, libpointer, .3, 3)
    testCase.verifyEqual(action2, 'forward')
        
    doAction(action2, motor_left, motor_right, libpointer, 2)
    
    testCase.verifyEqual(motor_left.Speed, 14)
    testCase.verifyEqual(motor_right.Speed, 14)
end

% Restart after stopping because of obstacle
% Car sensors see white
function test_tc3_3(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 91, 91, libpointer, libpointer, libpointer, .21, 3)
    testCase.verifyEqual(action, 'forward')
        
    doAction(action, motor_left, motor_right, libpointer, 2)
    
    testCase.verifyEqual(motor_left.Speed, 14)
    testCase.verifyEqual(motor_right.Speed, 14)
    end


