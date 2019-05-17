function [] = right(motor_left, motor_right, speed, time)
    motor_left.Speed = speed;
    motor_right.Speed = -speed * 0.50;
    pause(time)
    motor_left.Speed = 0;
    motor_right.Speed = 0;
    display("right")
end