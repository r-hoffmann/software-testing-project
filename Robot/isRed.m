function isRed = isRed(color, color_reflected, color_ambient)
    isRed = false;
    if(color_reflected < 90 && color_reflected > 70)
        isRed = true;
    end
end