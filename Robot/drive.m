function [] = drive()
    myrobot = legoev3('usb'); 

    motor_left = motor(myrobot, 'A');
    motor_right = motor(myrobot, 'B');

    colorsensor_left = colorSensor(myrobot, 1); 
    colorsensor_right = colorSensor(myrobot, 3); 

    ultrasonic_sensor = sonicSensor(myrobot);
    
    i = 0;
    while(i<10)
       i = i + 1; 
       [distance, color_left, color_right, color_reflected_left, color_reflected_right] = getSensors(ultrasonic_sensor, colorsensor_left, colorsensor_right)
       
       action = resolveAction(ultrasonic_sensor, colorsensor_left, colorsensor_right);
       doAction(action, motor_left, motor_right);
    end
    
end