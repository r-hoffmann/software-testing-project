function action = resolveAction(color_left, color_right, color_reflected_left, color_reflected_right)
    if(isWhite(color_left, color_reflected_left) && isWhite(color_right, color_reflected_right))
        action = 'forward';
        return;
    end
    
    if(isGreen(color_left, color_reflected_left) && isGreen(color_right, color_reflected_right))
        action = 'fastForward';
        return;
    end
    
    if(isGrey(color_left, color_reflected_left) && isGrey(color_right, color_reflected_right))
        action = 'slowForward';
        return;
    end
    
    if(isWhite(color_left, color_reflected_left) && ~isWhite(color_right, color_reflected_right))
        action = 'right';
        return;
    end
    
    if(~isWhite(color_left, color_reflected_left) && isWhite(color_right, color_reflected_right))
        action = 'left';
        return;
    end

    if(isPurple(color_left, color_reflected_left) && isPurple(color_right, color_reflected_right))
        action = 'getParkingSpot';
        return
    end
end
