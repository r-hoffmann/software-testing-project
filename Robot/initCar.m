function [motor_left, motor_right, colorsensor_left, colorsensor_right, ultrasonic_sensor] = initCar()
    clear;
    myrobot = legoev3('usb'); 

    motor_left = motor(myrobot, 'A');
    motor_right = motor(myrobot, 'B');
    
    start(motor_left);
    start(motor_right);

    colorsensor_left = colorSensor(myrobot, 1); 
    colorsensor_right = colorSensor(myrobot, 3); 

    ultrasonic_sensor = sonicSensor(myrobot);
end