function isBlack = isBlack(color, color_reflected, color_ambient)
    isBlack = false;   
    if(color_reflected < 25 && color_reflected >= 0)
       isBlack = true; 
    end
end