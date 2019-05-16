function [] = stop_motors(motor_left, motor_right)

    motor_left.Speed = 0;
    motor_right.Speed = 0;
    
    display("stop")
end