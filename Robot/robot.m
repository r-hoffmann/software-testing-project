%%
myrobot = legoev3('usb'); 

motor_left = motor(myrobot, 'A');
motor_right = motor(myrobot, 'B');

color_left = colorSensor(myrobot,1); 
color_right = colorSensor(myrobot,3); 

ultrasonic_sensor = sonicSensor(myrobot);
%%

forward(motor_left, motor_right, 10)
stop(motor_left, motor_right, 0)
left(motor_left, motor_right, 20, 3)
right(motor_left, motor_right, 20, 3)

[distance, col_left, col_right] = getSensors(ultrasonic_sensor, color_left, color_right);


clear myrobot;