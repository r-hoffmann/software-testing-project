function [] = drive()
    %LOGS = []
    
    parked = 0;
    prev_action = '';
    stage = 1;
    i = 0;
    % Currently just do 10 steps, should be while not parked.
    while(parked == 0)
       i = i + 1; 
       [distance, color_left, color_right, color_reflected_left, color_reflected_right, color_ambient_left, color_ambient_right] = getSensors(ultrasonic_sensor, colorsensor_left, colorsensor_right);
       
       action = resolveAction(color_left, color_right, color_reflected_left, color_reflected_right, prev_action);

       prev_action = doAction(action, motor_left, motor_right, ultrasonic_sensor, stage);
       
     %  log = [color_left, color_ight, action, prev_action]
      % LOGS = [LOGS; log]
    end 
    
    stop_motors(motor_left, motor_right)
    
end