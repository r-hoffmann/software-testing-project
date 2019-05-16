function [action] = doAction(action, motor_left, motor_right, ultrasonic_sensor)
    speed = 10;
    turn_speed = 30;
    turntime = .11;

    switch action
        case 'terminate'
            terminate();
        case 'forward'
            forward(motor_left, motor_right, speed);
        case 'fastForward'
            fastForward(motor_left, motor_right, speed, 1.5);
        case 'slowForward'
            fastForward(motor_left, motor_right, speed, 0.5);
        case 'right'
            right(motor_left, motor_right, turn_speed, turntime);
        case 'left'
            left(motor_left, motor_right, turn_speed, turntime);
        case 'stop'
            stop_motors(motor_left, motor_right);
        case 'parkLeft'
            parkLeft(motor_left, motor_right);
        case 'parkRight'
            parkRight(motor_left, motor_right);
        case 'getParkingSpot'
            action = getParkingSpot(motor_left, motor_right, ultrasonic_sensor);
            % resolved new action, execute it
            doAction(action, motor_left, motor_right, ultrasonic_sensor);
        case 'repeat'
            doAction(prev_action, motor_left, motor_right, ultrasonic_sensor); 
    end
end