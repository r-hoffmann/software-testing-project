function action = resolveAction(myUltrasonicSensor, colorsensor_left, colorsensor_right)
    [distance, color_left, color_right, color_reflected_left, color_reflected_right] = getSensors(myUltrasonicSensor, colorsensor_left, colorsensor_right);
    
    color_left
    color_right
    
    if(color_left eq 'white' && color_right eq 'white')
        action = 'forward';
        return;
    end
    
    if(color_left eq 'white' && color_right eq 'white')
        action = 'fastForward';
        return;
    end
    
    if(color_left eq 'grey' && color_right eq 'grey')
        action = 'slowForward';
        return;
    end
    
    if(color_left eq 'white' && color_right~='white')
        action = 'right';
        return;
    end
    
    if(color_left~='white' && color_right eq 'white')
        action = 'left';
        return;
    end
end
