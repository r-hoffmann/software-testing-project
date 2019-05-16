function [] = forward(motor_left, motor_right, speed)

    motor_left.Speed = speed;
    motor_right.Speed = speed;
    
    
    display("forward")
end



