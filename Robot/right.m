function [] = right(motor_left, motor_right, speed, time)
    left(motor_left, motor_right, -speed, time)
end