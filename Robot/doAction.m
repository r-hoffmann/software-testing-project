function [action, stage] = doAction(action, motor_left, motor_right, ultrasonic_sensor, stage)
    speed = 14;
    turn_speed = 30;
    turntime = .3;

    switch stage
        case 1
            speed = 30;
            turntime = .2;
            turn_speed = 10;
        case 2
            turntime = .15;
            turn_speed = 60;
        case 3
            speed = 10;
    end
    
    switch action
        case 'terminate'
            terminate();
        case 'forward'
            forward(motor_left, motor_right, speed);
        case 'fastForward'
            stage = 1;
            forward(motor_left, motor_right, speed);
        case 'slowForward'
            stage = 3;
            forward(motor_left, motor_right, speed);
        case 'right'
            right(motor_left, motor_right, turn_speed, turntime);
        case 'left'
            left(motor_left, motor_right, turn_speed, turntime);
        case 'stop'
            stop_motors(motor_left, motor_right);
        case 'parkLeft'
            parkLeft(motor_left, motor_right, 14, 0.5);
        case 'parkRight'
            parkRight(motor_left, motor_right, 14, 0.5);
        case 'getParkingSpot'
            action = getParkingSpot(motor_left, motor_right, ultrasonic_sensor);
            % resolved new action, execute it
            doAction(action, motor_left, motor_right, ultrasonic_sensor);
        case 'repeat'
            doAction(prev_action, motor_left, motor_right, ultrasonic_sensor); 
    end
end