function [] = test()
    myrobot = legoev3('usb'); 

    motor_left = motor(myrobot, 'A');
    motor_right = motor(myrobot, 'B');

    colorsensor_left = colorSensor(myrobot, 1); 
    colorsensor_right = colorSensor(myrobot, 3); 

    ultrasonic_sensor = sonicSensor(myrobot);
    
    [distance, color_left, color_right, color_reflected_left, color_reflected_right] = getSensors(ultrasonic_sensor, colorsensor_left, colorsensor_right);
    distance
    color_left
    color_right
    color_reflected_left
    color_reflected_right
end