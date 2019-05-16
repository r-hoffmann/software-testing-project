function [] = drive()
    clear;
    myrobot = legoev3('usb'); 

    motor_left = motor(myrobot, 'A');
    motor_right = motor(myrobot, 'B');
    
    start(motor_left);
    start(motor_right);

    colorsensor_left = colorSensor(myrobot, 1); 
    colorsensor_right = colorSensor(myrobot, 3); 

    ultrasonic_sensor = sonicSensor(myrobot);
    
    %LOGS = []
    
    parked = 0;
    % Currently just do 10 steps, should be while not parked.
    while(parked == 0)
       i = i + 1; 
       [distance, color_left, color_right, color_reflected_left, color_reflected_right] = getSensors(ultrasonic_sensor, colorsensor_left, colorsensor_right)
       
       action = resolveAction(color_left, color_right, color_reflected_left, color_reflected_right, prev_action);

       prev_action = doAction(action, motor_left, motor_right, ultrasonic_sensor);
       
     %  log = [color_left, color_right, action, prev_action]
      % LOGS = [LOGS; log]
    end 
    
    stop_motors(motor_left, motor_right)
    
end