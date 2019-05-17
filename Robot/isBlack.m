function isBlack = isBlack(color, color_reflected, color_ambient)
    isBlack = false;   
    if(color_reflected < 25)
       isBlack = true; 
    end
end