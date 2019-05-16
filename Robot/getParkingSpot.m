function action = getParkingSpot(motor_left, motor_right, ultrasonic_sensor)
    % Idea: Rotate left; check if empty. If empty, park there, else rotate right; check if empty, if empty, park there, else terminate.
    speed = 10
    time = 0.3
    
    left(motor_left, motor_right, speed, time);
    
    empty = checkIfEmpty(ultrasonic_sensor);
    if(empty)
        action = 'parkLeft';
        return;
    end
    
    right(motor_left, motor_right, speed, 2 * time);
    empty = checkIfEmpty(ultrasonic_sensor);
    if(empty)
        action = 'parkRight';
        return;
    end
    action = 'terminate';
end