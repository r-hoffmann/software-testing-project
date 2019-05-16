function [] = parkLeft(motor_left, motor_right, speed, time)
    % Go left
    left(motor_left, motor_right, speed, time)
    
    % Drive straight 2 seconds
    forward(motor_left, motor_right, speed)
    pause(2)
    forward(motor_left, motor_right, 0)

    % Realign
    right(motor_left, motor_right, speed, time)

    % Drive straight 2 seconds
    forward(motor_left, motor_right, speed)
    pause(2)
    forward(motor_left, motor_right, 0)

    display("parked left")
end