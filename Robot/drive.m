function [] = drive(motor_left, motor_right, colorsensor_left, colorsensor_right, ultrasonic_sensor)
    LOGS = []
    
    parked = 0;
    prev_action = '';
    stage = 2;
    
    % Currently just do 10 steps, should be while not parked.
    while(parked == 0)
       
       [distance, color_left, color_right, color_reflected_left, color_reflected_right, color_ambient_left, color_ambient_right] = getSensors(ultrasonic_sensor, colorsensor_left, colorsensor_right, stage);
       
       [action, stage] = resolveAction(color_left, color_right, color_reflected_left, color_reflected_right, color_ambient_left, color_ambient_right, prev_action, distance, stage);

       [prev_action, stage] = doAction(action, motor_left, motor_right, ultrasonic_sensor, stage);
       
       log = [color_reflected_left, color_reflected_right, color_ambient_left, color_ambient_right, stage];
       disp(action);
       disp(log);
    end 
end