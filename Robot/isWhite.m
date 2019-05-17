function isWhite = isWhite(color, color_reflected, color_ambient)
    isWhite = false;
    if(color_reflected >= 90)
       isWhite = true; 
    end
end