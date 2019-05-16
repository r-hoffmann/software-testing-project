function [] = doAction(action, motor_left, motor_right, ultrasonic_sensor)
    speed = 10;
    switch action
        case 'terminate'
            terminate();
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
        case 'parkLeft'
            parkLeft(motor_left, motor_right);
        case 'parkRight'
            parkRight(motor_left, motor_right);
        case 'getParkingSpot'
            action = getParkingSpot(motor_left, motor_right, ultrasonic_sensor);
            % resolved new action, execute it
            doAction(action, motor_left, motor_right, ultrasonic_sensor);
    end
end