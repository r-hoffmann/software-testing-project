clear;
[motor_left, motor_right, colorsensor_left, colorsensor_right, ultrasonic_sensor] = initCar()

drive(motor_left, motor_right, colorsensor_left, colorsensor_right, ultrasonic_sensor)

stop_motors(motor_left, motor_right)
for i = 1 : 10
tic
[distance, color_left, color_right, color_reflected_left, color_reflected_right, color_ambient_left, color_ambient_right] = getSensors(ultrasonic_sensor, colorsensor_left, colorsensor_right, stage)
toc
end
