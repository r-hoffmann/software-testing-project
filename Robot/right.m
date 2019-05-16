function [] = right(motor_left, motor_right, speed, time)
    motor_left.Speed = speed * 0.75;
    motor_right.Speed = -speed;
    pause(time)
    motor_left.Speed = 0;
    motor_right.Speed = 0;
    display("right")
end