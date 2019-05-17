function [] = fastForward(motor_left, motor_right, speed, multiplier)
    forward(motor_left, motor_right, speed * multiplier);
    stage = 2;
end