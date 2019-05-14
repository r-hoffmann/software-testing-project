function [] = doAction(action, motor_left, motor_right)
    speed = 10;
    switch action
        case 'forward'
            forward(motor_left, motor_right, speed);
        case 'fastForward'
            fastForward(motor_left, motor_right, speed);
        case 'slowForward'
            fastForward(motor_left, motor_right, speed);
        case 'right'
            right(motor_left, motor_right, speed);
        case 'left'
            left(motor_left, motor_right, speed);
        case 'stop'
            stop(motor_left, motor_right);
    end
end