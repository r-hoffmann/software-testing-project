function [distance, color_left, color_right, color_reflected_left, color_reflected_right, color_ambient_left, color_ambient_right] = getSensors(ultrasonic_sensor, colorsensor_left, colorsensor_right)
    distance = readDistance(ultrasonic_sensor);
    color_left = readColor(colorsensor_left);
    color_right = readColor(colorsensor_right);
    color_reflected_left = readLightIntensity(colorsensor_left, 'reflected');
    color_reflected_right = readLightIntensity(colorsensor_right, 'reflected');
    color_ambient_left = readLightIntensity(colorsensor_left);
    color_ambient_right = readLightIntensity(colorsensor_right);
end