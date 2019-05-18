function [action, stage] = resolveAction(color_left, color_right, color_reflected_left, color_reflected_right, color_ambient_left, color_ambient_right, prev_action, distance, stage)

    if(obstacleInRange(distance, stage))
       action = 'stop';
       return
    end
    
    if(stage == 1 && (isWhite(color_left, color_reflected_left, color_ambient_left) && isWhite(color_right, color_reflected_right, color_ambient_right)))
        stage = 2;
     end

    if(stage == 3 && (isWhite(color_left, color_reflected_left, color_ambient_left) && isWhite(color_right, color_reflected_right, color_ambient_right)))
       stage = 4; 
    end
    
    % if(isBlack(color_left, color_reflected_left, color_ambient_left) && isBlack(color_right, color_reflected_right, color_ambient_right))
    %     if  prev_action == "left" || prev_action == "right"
    %         action = "repeat";
    %     end
        
    % end
    
    if(isWhite(color_left, color_reflected_left, color_ambient_left) & isWhite(color_right, color_reflected_right, color_ambient_right))
        action = 'forward';
        return;
    end
    
    if(isBlack(color_left, color_reflected_left, color_ambient_left) & isBlack(color_right, color_reflected_right, color_ambient_right))
        action = 'forward';
        return;
    end
        
    if(isRed(color_left, color_reflected_left, color_ambient_left) & isRed(color_right, color_reflected_right, color_ambient_right))
        action = 'fastForward';
        return;
    end
    
    [isGrey_left, isPurple_left] = isGreyOrPurple(color_left, color_reflected_left, color_ambient_left, stage);
    [isGrey_right, isPurple_right] = isGreyOrPurple(color_right, color_reflected_right, color_ambient_right, stage);
    if(isGrey_left & isGrey_right)
        stage = 3;
        action = 'slowForward';
        return;
    end
    
 
    if(isWhite(color_left, color_reflected_left, color_ambient_left) & ~isWhite(color_right, color_reflected_right, color_ambient_right))
        action = 'right';
        return;
    end
    
    if(~isWhite(color_left, color_reflected_left, color_ambient_left)& isWhite(color_right, color_reflected_right, color_ambient_right))
        action = 'left';
        return;
    end
    
    
    if(isRed(color_left, color_reflected_left, color_ambient_left) & ~isRed(color_right, color_reflected_right, color_ambient_right))
        action = 'right';
        return;
    end
    
    if(~isRed(color_left, color_reflected_left, color_ambient_left) & isRed(color_right, color_reflected_right, color_ambient_right))
        action = 'left';
        return;
    end

    if(isGrey_left & isBlack(color_right, color_reflected_right, color_ambient_right))
        action = 'right';
        return;
    end
    
    if(~isBlack(color_left, color_reflected_left, color_ambient_left) & isGrey_right)
        action = 'left';
        return;
    end
    
    if(isPurple_left & isPurple_right)
        action = 'getParkingSpot';
        return
    end
    
    action = 'stop';
end
