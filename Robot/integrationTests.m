function tests = integrationTests
    tests = functiontests(localfunctions);
end

% 
% function test_tc1_1(testCase)
%     motor_left = dummyMotor()
%     motor_right = dummyMotor()
% 
%     action = resolveAction(libpointer, libpointer, 90, 90, libpointer, libpointer, libpointer, .3, libpointer)
%     testCase.verifyEqual(action, 'forward')
%         
%     doAction(action, motor_left, motor_right, libpointer, 2)
%     
%     testCase.verifyEqual(motor_left.Speed, 14)
%     testCase.verifyEqual(motor_right.Speed, 14)
% end
% 
% % 
% function test_tc1_2(testCase)
%     motor_left = dummyMotor()
%     motor_right = dummyMotor()
% 
%     action = resolveAction(libpointer, libpointer, 75, 75, libpointer, libpointer, libpointer, .3, libpointer)
%     testCase.verifyEqual(action, 'fastForward')
%         
%     doAction(action, motor_left, motor_right, libpointer, 1)
%     
%     testCase.verifyEqual(motor_left.Speed, 30)
%     testCase.verifyEqual(motor_right.Speed, 30)
% end
% 
% % 
% function test_tc1_3(testCase)
%     motor_left = dummyMotor()
%     motor_right = dummyMotor()
% 
%     action = resolveAction(libpointer, libpointer, 40, 40, libpointer, libpointer, libpointer, .3, libpointer)
%     testCase.verifyEqual(action, 'slowForward')
%         
%     doAction(action, motor_left, motor_right, libpointer, 3)
%     
%     testCase.verifyEqual(motor_left.Speed, 10)
%     testCase.verifyEqual(motor_right.Speed, 10)
% end
% 
% % 
% function test_tc1_5(testCase)
%     motor_left = dummyMotor()
%     motor_right = dummyMotor()
% 
%     action = resolveAction(libpointer, libpointer, 101, 101, libpointer, libpointer, libpointer, .3, libpointer)
%     testCase.verifyEqual(action, 'stop')
%         
%     doAction(action, motor_left, motor_right, libpointer, 3)
%     
%     testCase.verifyEqual(motor_left.Speed, 0)
%     testCase.verifyEqual(motor_right.Speed, 0)
% end
% 
% 




function test_tc2_1(testCase)
    motor_left = dummyMotor()
    motor_right = dummyMotor()

    action = resolveAction(libpointer, libpointer, 23, 26, libpointer, libpointer, libpointer, .3, libpointer)
    testCase.verifyEqual(action, 'left')
        
    doAction(action, motor_left, motor_right, libpointer, 3)
    
%     testCase.verifyEqual(motor_left.Speed, 0)
%     testCase.verifyEqual(motor_right.Speed, 0)
end




