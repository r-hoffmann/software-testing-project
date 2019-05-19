function [isGrey, isPurple] = isGreyOrPurple(color, color_reflected, color_ambient, stage)
    isGrey = false;
    isPurple = false;
    
    if(color_reflected > 30 && color_reflected < 50)
        if(stage == 4)
            isPurple = true;
        else
            isGrey = true;
        end
    end
end